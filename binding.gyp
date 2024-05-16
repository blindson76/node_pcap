{
  "variables":{
    "openssl_fips": "0"
  },
  "targets": [
    {
      "target_name": "pcap_binding",
      "sources": [ "pcap_binding.cc", "pcap_session.cc" ],
      "include_dirs": [
        "<!(node -e \"require('nan')\")"
      ],
      "link_settings": {
          "libraries": [
              "-lpcap"
          ]
      },
      "variables":{
        "openssl_fips": "0"
      }
    }
  ]
}
