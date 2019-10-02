'use strict';

require('sugar')();

var mysql = require('mysql');

var invalid_reasons_map = require('./lib/reason-map.js');

var additional_invalid = {
  employer_left_state: "Employer left State",
  employer_cannot_be_located: "Employer Cannot be Located",
  complainant_cannot_be_located: "Complainant Cannot be Located",
  complainant_dropped_claim: "Complainant Dropped Claim",
  paid_prior_to_investigation: "Paid Prior to Investigation",
  business_is_closed: "Business is Closed",
};

var conn = mysql.createConnection({
  host     : 'localhost',
  user     : 'root',
  password : 'root',
  database : 'lajc-claims'
});

conn.connect(function (err) {
  if (err) {
    console.error(err);
  }
});

conn.query('SELECT * FROM raw_data', function (err, results, fields) {
  if (err) {
    console.error(err);
    return;
  }

  results.forEach(function (r) {
    var invalid_reasons = [];

    if (r.claim_inval_other_description !== 'NA') {
      invalid_reasons.push(r.claim_inval_other_description);
    }

    if (r.claim_undetermined_other_description !== 'NA') {
      invalid_reasons.push(r.claim_undetermined_other_description);
    }

    Object.keys(additional_invalid).forEach(function (column) {
      if (r[column] !== 'NA') {
        invalid_reasons.push(additional_invalid[column]);
      }
    });

    invalid_reasons = invalid_reasons.map(function (reason) {
      return reason.titleize().replace(/\bVa\b/, 'VA');
    });

    invalid_reasons = Object.keys(invalid_reasons_map).filter(function (reason_key) {
      return invalid_reasons_map[reason_key].some(function (regex) {
        return invalid_reasons.some(function (reason) {
          return regex.test(reason);
        });
      })
    });

    if (invalid_reasons.length > 0) {
      // console.log(r.claim_no, invalid_reasons);
      console.log('"' + invalid_reasons[0] + '", ')
    }
  });
});