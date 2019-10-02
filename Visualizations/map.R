# Map 8-sections

library(sf)
library(tidycensus)
library(leaflet)
library(magrittr)
library(tidyverse)

dat <- read_csv("Raw data/lajc_clean.csv")

regions <- read_csv("Raw data/county_region.csv") %>% 
  slice(-(134:141)) %>% 
  mutate(type = str_replace(type, "Cities", "city") %>% 
           str_replace("Counties", "county")) %>% 
  unite(name, name, type, sep = " ") %>% 
  mutate(name = tolower(name))

# run this block once to save API calls
# options(tigris_use_cache = TRUE)
va <- get_acs(
  state = "VA", geography = "county",
  variables = "B19013_001", geometry = TRUE
  )

st_write(va, "Raw data/va.shp")

va_clean <- va %>% 
  rename_all(snakecase::to_snake_case) %>% 
  separate(name, c("name", "state"), sep = ", ") %>% 
  mutate(name = tolower(name))

anti_join(va_clean, regions)
anti_join(regions, va_clean)

va_clean %<>% inner_join(regions)

# ggplot version
ggplot(va_clean, aes(fill = region)) +
  geom_sf()

# leaflet version
pal <- colorFactor("Dark2", unique(va_clean$region))
leaflet(va_clean) %>% 
  addProviderTiles(provider = "Stamen.TonerLite",
                   group = "Stamen Toner") %>% 
  addPolygons(fillColor = ~pal(region), color = ~pal(region),
              popup = ~paste(name, "<br>", region))
