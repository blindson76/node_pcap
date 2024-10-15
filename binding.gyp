{
  "variables":{
    "openssl_fips": "0"
  },
  "targets": [
    {
      "target_name": "pcap_binding",
      "sources": [ "pcap_binding.cc", "pcap_session.cc" ],
      "include_dirs": [
        "<!(node -e \"require('nan')\")",
        "C:\\Users\\ubozkurt\\Downloads\\WpdPack_4_1_2\\WpdPack\\Include"
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
