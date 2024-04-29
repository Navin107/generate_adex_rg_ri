vv = [
      {
        "@context": "https://voc.iudx.org.in/",
        "id": "68593b2b-00e4-4a90-a74f-ddf6840d32d8",
        "id_bck": "imd.gov.in/d7733b0c544dfb3137767e5efa2c1ccd3b069bf8/rs.adex.org.in/agromet-imd/advisory-subdistrict-data",
        "type": [
          "adex:Resource",
          "adex:AgriAdvisory",
          "iudx:Resource",
          "iudx:AgriAdvisory"
        ],
        "name": "advisory-subdistrict-data",
        "label": "Agriculture Subdistrict (ASD) Level Agromet Advisory Data in Telangana State",
        "description": "Publishes expert advisory from Agromet (Agricultural Meterology Division) about weather, crop cultivation, pest control, livestock rearing etc. for the welfare of farmers, every Tuesdays and Fridays, for various mandals (ASD) of Telangana state.",
        "tags": [
          "Advisory",
          "district",
          "crop",
          "subdistrict",
          "general advisory",
          "state advisory",
          "regional advisory"
        ],
        "accessPolicy": "OPEN",
        "apdURL": "acl-apd.adex.org.in",
        "provider": "e0adf587-8210-406d-8c59-8c0f27e147af",
        "provider_bck": "imd.gov.in/d7733b0c544dfb3137767e5efa2c1ccd3b069bf8",
        "resourceServer": "41bb4389-ebaf-4df7-a575-556ec6092a25",
        "resourceGroup": "5d97f1bc-d548-4d02-9fd1-0e6d0f8227dd",
        "resourceGroup_bck": "imd.gov.in/d7733b0c544dfb3137767e5efa2c1ccd3b069bf8/rs.adex.org.in/agromet-imd",
        "resourceType": "MESSAGESTREAM",
        "adexResourceAPIs": [
          "ATTR",
          "TEMPORAL"
        ],
        "iudxResourceAPIs": [
          "ATTR",
          "TEMPORAL"
        ],
        "dataDescriptor": {
          "@context": "https://agrijson.org/",
          "type": [
            "iudx:DataDescriptor",
            "iudx:AgriAdvisory",
            "adex:DataDescriptor",
            "adex:AgriAdvisory"
          ],
          "dataDescriptorLabel": "Data descriptor for Agromet Advisory data Information at mandal (ASD) level in Telangana State",
          "description": "Data attribute details of Agromet Advisory data Information at mandal (ASD) level in Telangana State.",
          "stateCode": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "The state code corresponding to this observation..",
            "dataSchema": "iudx:Text"
          },
          "stateName": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "Name of the state corresponding to this observation.",
            "dataSchema": "iudx:Text"
          },
          "districtCode": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "The district code corresponding to this observation.",
            "dataSchema": "iudx:Text"
          },
          "districtName": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "Name of the district corresponding to this observation.",
            "dataSchema": "iudx:Text"
          },
          "subdistrictCode": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "The subdistrict code corresponding to this observation.",
            "dataSchema": "iudx:Text"
          },
          "subdistrictName": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "Name of the subdistrict corresponding to this observation. A subdistrict is also called as a tehsil, mandal, tahsil, tahasil, taluka, taluk, or taluq across the Indian states.",
            "dataSchema": "iudx:Text"
          },
          "commodityCode": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "The unique code for the commodity corresponding to this observation.",
            "dataSchema": "iudx:Text"
          },
          "commodityName": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "The common/local name of the commodity corresponding to the observation.",
            "dataSchema": "iudx:Text"
          },
          "agriculturalCategory": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "The name of the agricultural category corresponding to this observation. ENUM['crop',  'horticulture', 'livestock', 'fisheries', 'Poultry', 'others (Soil / Land Preparation)', 'sericulture'].",
            "dataSchema": "iudx:Text"
          },
          "regionalLangID": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "The unique ID representing the regional language of the location corresponding to this observation.",
            "dataSchema": "iudx:Text"
          },
          "regionalLangName": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "The name of the regional language corresponding to this observation.",
            "dataSchema": "iudx:Text"
          },
          "generalAdvisory": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "A general advisory to the farmers, for the cultivation of crops in regards to the conditions of weather, soil ,land etc. It may include warnings of potential catastrophical events.",
            "dataSchema": "iudx:Text"
          },
          "generalAdvisoryRegional": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "A general advisory, provided in the regional language, to the farmers for the cultivation of crops in regards to the conditions of weather, soil ,land etc. It may include warnings of potential catastrophical events.",
            "dataSchema": "iudx:Text"
          },
          "smsAdvisory": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "The advisory which has been communicated to farmers via messaging (SMS).",
            "dataSchema": "iudx:Text"
          },
          "smsAdvisoryRegional": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "The advisory which has been communicated to farmers in their regional language, via messaging (SMS).",
            "dataSchema": "iudx:Text"
          },
          "technicalAdvisory": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "An advisory to the farmers for the cultivation of a specific crop or rearing of livestock or about better agricultural practices corresponding to this observation.",
            "dataSchema": "iudx:Text"
          },
          "technicalAdvisoryRegional": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "An advisory, provided in the regional language, to the farmers for the cultivation of a specific crop corresponding to this observation.",
            "dataSchema": "iudx:Text"
          },
          "weatherSummary": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "A brief on how the weather has been in the past and/or is to be in the near future and/or is to prevail for the current day.",
            "dataSchema": "iudx:Text"
          },
          "weatherSummaryRegional": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "A brief provided in the regional language on how the weather has been in the past and/or is to be in the near future and/or is to prevail for the current day.",
            "dataSchema": "iudx:Text"
          },
          "observationDateTime": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "Last reported time of observation.",
            "dataSchema": "adex:DateTime"
          }
        },
        "dataSample": {
          "observationDateTime": "2023-07-14T00:00:00+05:30",
          "agriculturalCategory": "Horticulture",
          "stateCode": "36",
          "stateName": "Telangana",
          "districtCode": "541",
          "districtName": "KHAMMAM",
          "subdistrictCode": "199",
          "subdistrictName": "Khammam-Urban",
          "commodityCode": "580",
          "commodityName": "CHILLI",
          "regionalLangID": "13",
          "regionalLangName": "Telugu",
          "generalAdvisory": "Total normal rainfall of Khammam district is 227.8 mm and actual rainfall is 121.0 mm from 1st June to 14th July. Go for sowing of rice nursery after 24 hours of seed treatment with 3g Carbendazim per kg for dry seed or 1g per kg for wet seed helps in reducing of seed borne diseases. Farmers have started the sowing of cotton, green gram, maize under soil dry conditions and raising of rice nursery wherever sufficient irrigation is available.",
          "generalAdvisoryRegional": "ఖమ్మం జిల్లాలో జూన్ 01 నుండి జూలై 14 వరుకు సాధారణ వర్షపాతం 227.8 మి.మీ. కాగా ప్రస్తుతం 121.0 మి.మీ.ల వర్షం కురిసింది. కిలో పొడి వరి విత్తనానికి 3 గ్రా. కార్బండిజమ్ లేదా తడి విత్తనానికి 1 గ్రా. మందుతో విత్తన శుద్ధిచేసి 24 గంటల తర్వాత నారు మడిలో విత్తుకోవటం వలన నేల ద్వారా సంక్రమించే తెగుళ్ళను నివారించవచ్చు.",
          "smsAdvisory": "To control sucking pests in vegetable crops, spray Dimethoate 2 ml or Acephate 1.5 g or Acetamiprid 0.25 g per liter of water.",
          "smsAdvisoryRegional": "కూరగాయ పంటలలో రసంపీల్చే పురుగుల నివారణకు  లేదా డైమిథోయేట్ 2 మి.లీ లేదా ఎసిఫేట్ 1.5 గ్రా. లేదా ఎసిటామిప్రిడ్ 0.25 గ్రా. నీటికి కలిపి పిచికారి చేయాలి.",
          "technicalAdvisory": "Farmers are suggested to go for rising of chilli nursery from July 1st week to August second week. Make sure not to stand water in the nursery. To control damping off in chilli nursery make soil drenching with  3g Metalaxyl or Copper oxychloride or 2.5g Ridomil MZ per litre of water immediately after emergence of seedlings.",
          "technicalAdvisoryRegional": "రైతు సోదరులు మిరప నారును జులై మొదటి వారం నుంచి  ఆగష్టు రెండవ వారం వరకు పోసుకోవచ్చును. నారు మడిలో నీరు నిల్వ ఉండకుండా చేయాలి. మిరపలో నారు కుళ్ళు నివారణకు గింజలు మొలకెత్తిన వెంటనే  3 గ్రా. కాపర్ ఆక్సీ క్లోరైడ్ లేదా 2.5 గ్రా. రెడోమిల్ యం.జడ్. లీటరు నీటికి కలిపి పూర్తిగా తడపాలి.",
          "weatherSummary": "During last three days fairly wide spread light to moderate rainfall received in the district. In the upcoming five days cloudy weather with light to moderate rainfall likely to occur at few places in the district. The maximum & minimum temperature range might be 34.1 – 35.5 deg and 23.6 – 25.5 deg. centigrade, respectively. As per the extended range forecast system (ERFS) above normal rainfall, below normal day and normal night temperature might be expected during 19th July to 25nd July in Telangana state. ",
          "weatherSummaryRegional": "జిల్లాలో గత మూడు రోజులు తేలికపాటి నుంచి మోస్తరు వర్షాలు చాలా చోట్ల కురిసాయి. జిల్లాలో ఈ రోజు నుంచి రాగల నాలుగు రోజుల వరకు ఆకాశం మేఘావృతమై ఉండి, తేలికపాటి నుంచి మోస్తరు వర్షాలు కొన్నిచోట్ల కురిసే అవకాశం ఉంది. పగటి మరియు రాత్రి ఉష్ణోగ్రతలు 34.1 – 35.5 డి. సెం. మరియు 23.6– 25.3 డి. సెం. గా నమోదయ్యే సూచన కలదు. ERFS ముందస్తు వాతావరణ సమాచారం ప్రకారం తెలంగాణలో జూలై 19 నుంచి జూలై 25 వరకు సాధారణం కంటే ఎక్కువ వర్షపాతం మరియు సాధారణం కంటే తక్కువ పగటి & రాత్రి ఉష్ణోగ్రతలు నమోదయ్యే సూచన కలదు. "
        },
        "location": {
          "geometry": {
            "coordinates": [
              [
                [
                  77.179011,
                  18.556975
                ],
                [
                  77.047585,
                  15.14819
                ],
                [
                  81.059914,
                  16.55208
                ],
                [
                  81.384916,
                  17.721272
                ],
                [
                  80.569225,
                  19.514793
                ],
                [
                  78.217742,
                  20.06644
                ],
                [
                  77.179011,
                  18.556975
                ]
              ]
            ],
            "type": "Polygon"
          },
          "type": "Place",
          "address": "Telangana"
        },
        "itemStatus": "ACTIVE",
        "ownerUserId": "504f246c-4130-451f-b4df-ce41e245a754",
        "cos": "49f96c4c-e595-4fee-984c-43dededfba48",
        "itemCreatedAt": "2024-01-01T11:26:44+0530"
      },
      {
        "@context": "https://voc.iudx.org.in/",
        "id": "404aae9f-905f-41de-b938-a7dccf013d9d",
        "id_bck": "imd.gov.in/d7733b0c544dfb3137767e5efa2c1ccd3b069bf8/rs.adex.org.in/agromet-imd/advisory-district-data",
        "type": [
          "adex:Resource",
          "adex:AgriAdvisory",
          "iudx:Resource",
          "iudx:AgriAdvisory"
        ],
        "name": "advisory-district-data",
        "label": "District Level Agromet Advisory Data in Telangana State",
        "description": "Publishes expert advisory from Agromet (Agricultural Meterology Division) about weather, crop cultivation, pest control, livestock rearing etc. for the welfare of farmers, every Tuesdays and Fridays, for various districts of Telangana state.",
        "tags": [
          "Advisory",
          "district",
          "crop",
          "subdistrict",
          "general advisory",
          "state advisory",
          "regional advisory"
        ],
        "accessPolicy": "OPEN",
        "apdURL": "acl-apd.adex.org.in",
        "provider": "e0adf587-8210-406d-8c59-8c0f27e147af",
        "provider_bck": "imd.gov.in/d7733b0c544dfb3137767e5efa2c1ccd3b069bf8",
        "resourceServer": "41bb4389-ebaf-4df7-a575-556ec6092a25",
        "resourceGroup": "5d97f1bc-d548-4d02-9fd1-0e6d0f8227dd",
        "resourceGroup_bck": "imd.gov.in/d7733b0c544dfb3137767e5efa2c1ccd3b069bf8/rs.adex.org.in/agromet-imd",
        "resourceType": "MESSAGESTREAM",
        "adexResourceAPIs": [
          "ATTR",
          "TEMPORAL"
        ],
        "iudxResourceAPIs": [
          "ATTR",
          "TEMPORAL"
        ],
        "dataDescriptor": {
          "@context": "https://agrijson.org/",
          "type": [
            "iudx:DataDescriptor",
            "iudx:AgriAdvisory",
            "adex:DataDescriptor",
            "adex:AgriAdvisory"
          ],
          "dataDescriptorLabel": "Data descriptor for Agromet Advisory data Information at district level in Telangana State",
          "description": "Data attribute details of Agromet Advisory data Information at district level in Telangana State.",
          "stateCode": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "The state code corresponding to this observation..",
            "dataSchema": "iudx:Text"
          },
          "stateName": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "Name of the state corresponding to this observation.",
            "dataSchema": "iudx:Text"
          },
          "districtCode": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "The district code corresponding to this observation.",
            "dataSchema": "iudx:Text"
          },
          "districtName": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "Name of the district corresponding to this observation.",
            "dataSchema": "iudx:Text"
          },
          "commodityCode": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "The unique code for the commodity corresponding to this observation.",
            "dataSchema": "iudx:Text"
          },
          "commodityName": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "The common/local name of the commodity corresponding to the observation.",
            "dataSchema": "iudx:Text"
          },
          "agriculturalCategory": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "The name of the agricultural category corresponding to this observation. ENUM['crop',  'horticulture', 'livestock', 'fisheries', 'Poultry', 'others (Soil / Land Preparation)', 'sericulture'].",
            "dataSchema": "iudx:Text"
          },
          "regionalLangID": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "The unique ID representing the regional language of the location corresponding to this observation.",
            "dataSchema": "iudx:Text"
          },
          "regionalLangName": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "The name of the regional language corresponding to this observation.",
            "dataSchema": "iudx:Text"
          },
          "generalAdvisory": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "A general advisory to the farmers, for the cultivation of crops in regards to the conditions of weather, soil ,land etc. It may include warnings of potential catastrophical events.",
            "dataSchema": "iudx:Text"
          },
          "generalAdvisoryRegional": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "A general advisory, provided in the regional language, to the farmers for the cultivation of crops in regards to the conditions of weather, soil ,land etc. It may include warnings of potential catastrophical events.",
            "dataSchema": "iudx:Text"
          },
          "smsAdvisory": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "The advisory which has been communicated to farmers via messaging (SMS).",
            "dataSchema": "iudx:Text"
          },
          "smsAdvisoryRegional": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "The advisory which has been communicated to farmers in their regional language, via messaging (SMS).",
            "dataSchema": "iudx:Text"
          },
          "technicalAdvisory": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "An advisory to the farmers for the cultivation of a specific crop or rearing of livestock or about better agricultural practices corresponding to this observation.",
            "dataSchema": "iudx:Text"
          },
          "technicalAdvisoryRegional": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "An advisory, provided in the regional language, to the farmers for the cultivation of a specific crop corresponding to this observation.",
            "dataSchema": "iudx:Text"
          },
          "weatherSummary": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "A brief on how the weather has been in the past and/or is to be in the near future and/or is to prevail for the current day.",
            "dataSchema": "iudx:Text"
          },
          "weatherSummaryRegional": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "A brief provided in the regional language on how the weather has been in the past and/or is to be in the near future and/or is to prevail for the current day.",
            "dataSchema": "iudx:Text"
          },
          "observationDateTime": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "Last reported time of observation.",
            "dataSchema": "adex:DateTime"
          }
        },
        "dataSample": {
          "observationDateTime": "2023-07-14T00:00:00+05:30",
          "agriculturalCategory": "Horticulture",
          "stateCode": "36",
          "stateName": "Telangana",
          "districtCode": "541",
          "districtName": "KHAMMAM",
          "commodityCode": "580",
          "commodityName": "CHILLI",
          "regionalLangID": "13",
          "regionalLangName": "Telugu",
          "generalAdvisory": "Total normal rainfall of Khammam district is 227.8 mm and actual rainfall is 121.0 mm from 1st June to 14th July. Go for sowing of rice nursery after 24 hours of seed treatment with 3g Carbendazim per kg for dry seed or 1g per kg for wet seed helps in reducing of seed borne diseases. Farmers have started the sowing of cotton, green gram, maize under soil dry conditions and raising of rice nursery wherever sufficient irrigation is available.",
          "generalAdvisoryRegional": "ఖమ్మం జిల్లాలో జూన్ 01 నుండి జూలై 14 వరుకు సాధారణ వర్షపాతం 227.8 మి.మీ. కాగా ప్రస్తుతం 121.0 మి.మీ.ల వర్షం కురిసింది. కిలో పొడి వరి విత్తనానికి 3 గ్రా. కార్బండిజమ్ లేదా తడి విత్తనానికి 1 గ్రా. మందుతో విత్తన శుద్ధిచేసి 24 గంటల తర్వాత నారు మడిలో విత్తుకోవటం వలన నేల ద్వారా సంక్రమించే తెగుళ్ళను నివారించవచ్చు.",
          "smsAdvisory": "To control sucking pests in vegetable crops, spray Dimethoate 2 ml or Acephate 1.5 g or Acetamiprid 0.25 g per liter of water.",
          "smsAdvisoryRegional": "కూరగాయ పంటలలో రసంపీల్చే పురుగుల నివారణకు  లేదా డైమిథోయేట్ 2 మి.లీ లేదా ఎసిఫేట్ 1.5 గ్రా. లేదా ఎసిటామిప్రిడ్ 0.25 గ్రా. నీటికి కలిపి పిచికారి చేయాలి.",
          "technicalAdvisory": "Farmers are suggested to go for rising of chilli nursery from July 1st week to August second week. Make sure not to stand water in the nursery. To control damping off in chilli nursery make soil drenching with  3g Metalaxyl or Copper oxychloride or 2.5g Ridomil MZ per litre of water immediately after emergence of seedlings.",
          "technicalAdvisoryRegional": "రైతు సోదరులు మిరప నారును జులై మొదటి వారం నుంచి  ఆగష్టు రెండవ వారం వరకు పోసుకోవచ్చును. నారు మడిలో నీరు నిల్వ ఉండకుండా చేయాలి. మిరపలో నారు కుళ్ళు నివారణకు గింజలు మొలకెత్తిన వెంటనే  3 గ్రా. కాపర్ ఆక్సీ క్లోరైడ్ లేదా 2.5 గ్రా. రెడోమిల్ యం.జడ్. లీటరు నీటికి కలిపి పూర్తిగా తడపాలి.",
          "weatherSummary": "During last three days fairly wide spread light to moderate rainfall received in the district. In the upcoming five days cloudy weather with light to moderate rainfall likely to occur at few places in the district. The maximum & minimum temperature range might be 34.1 – 35.5 deg and 23.6 – 25.5 deg. centigrade, respectively. As per the extended range forecast system (ERFS) above normal rainfall, below normal day and normal night temperature might be expected during 19th July to 25nd July in Telangana state. ",
          "weatherSummaryRegional": "జిల్లాలో గత మూడు రోజులు తేలికపాటి నుంచి మోస్తరు వర్షాలు చాలా చోట్ల కురిసాయి. జిల్లాలో ఈ రోజు నుంచి రాగల నాలుగు రోజుల వరకు ఆకాశం మేఘావృతమై ఉండి, తేలికపాటి నుంచి మోస్తరు వర్షాలు కొన్నిచోట్ల కురిసే అవకాశం ఉంది. పగటి మరియు రాత్రి ఉష్ణోగ్రతలు 34.1 – 35.5 డి. సెం. మరియు 23.6– 25.3 డి. సెం. గా నమోదయ్యే సూచన కలదు. ERFS ముందస్తు వాతావరణ సమాచారం ప్రకారం తెలంగాణలో జూలై 19 నుంచి జూలై 25 వరకు సాధారణం కంటే ఎక్కువ వర్షపాతం మరియు సాధారణం కంటే తక్కువ పగటి & రాత్రి ఉష్ణోగ్రతలు నమోదయ్యే సూచన కలదు. "
        },
        "location": {
          "geometry": {
            "coordinates": [
              [
                [
                  77.179011,
                  18.556975
                ],
                [
                  77.047585,
                  15.14819
                ],
                [
                  81.059914,
                  16.55208
                ],
                [
                  81.384916,
                  17.721272
                ],
                [
                  80.569225,
                  19.514793
                ],
                [
                  78.217742,
                  20.06644
                ],
                [
                  77.179011,
                  18.556975
                ]
              ]
            ],
            "type": "Polygon"
          },
          "type": "Place",
          "address": "Telangana"
        },
        "itemStatus": "ACTIVE",
        "ownerUserId": "504f246c-4130-451f-b4df-ce41e245a754",
        "cos": "49f96c4c-e595-4fee-984c-43dededfba48",
        "itemCreatedAt": "2024-01-01T11:26:47+0530"
      },
      {
        "@context": "https://voc.iudx.org.in/",
        "id": "9b8ec594-a9e9-4b43-a13a-d8e0b0c54866",
        "id_bck": "imd.gov.in/d7733b0c544dfb3137767e5efa2c1ccd3b069bf8/rs.adex.org.in/agromet-imd/commodity-codes",
        "type": [
          "adex:Resource",
          "adex:AgriAdvisory",
          "iudx:Resource",
          "iudx:AgriAdvisory"
        ],
        "name": "commodity-codes",
        "label": "Commodity Codes for Agromet Advisory Data in Telangana State",
        "description": "Publishes commodity data information such as commodity code and commodity name for various districts and mandals (ASD) of Telangana state.",
        "tags": [
          "Advisory",
          "district",
          "crop",
          "commodity",
          "data",
          "code"
        ],
        "accessPolicy": "OPEN",
        "apdURL": "acl-apd.adex.org.in",
        "provider": "e0adf587-8210-406d-8c59-8c0f27e147af",
        "provider_bck": "imd.gov.in/d7733b0c544dfb3137767e5efa2c1ccd3b069bf8",
        "resourceServer": "41bb4389-ebaf-4df7-a575-556ec6092a25",
        "resourceGroup": "5d97f1bc-d548-4d02-9fd1-0e6d0f8227dd",
        "resourceGroup_bck": "imd.gov.in/d7733b0c544dfb3137767e5efa2c1ccd3b069bf8/rs.adex.org.in/agromet-imd",
        "resourceType": "DATASET",
        "adexResourceAPIs": [
          "ATTR"
        ],
        "iudxResourceAPIs": [
          "ATTR"
        ],
        "dataDescriptor": {
          "@context": "https://agrijson.org/",
          "type": [
            "iudx:DataDescriptor",
            "iudx:AgriAdvisory",
            "adex:DataDescriptor",
            "adex:AgriAdvisory"
          ],
          "dataDescriptorLabel": "Data descriptor for Agromet Advisory Commodity Data Information for various district and mandals (ASD) in Telangana State",
          "description": "Data attribute details of agromet advisory commodity data information for various district and mandals (ASD) in Telangana State.",
          "commodityCode": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "The unique code for the commodity corresponding to this observation.",
            "dataSchema": "iudx:Text"
          },
          "commodityName": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "The common/local name of the commodity corresponding to the observation.",
            "dataSchema": "iudx:Text"
          }
        },
        "dataSample": {
          "commodityCode": "580",
          "commodityName": "CHILLI"
        },
        "location": {
          "geometry": {
            "coordinates": [
              [
                [
                  77.179011,
                  18.556975
                ],
                [
                  77.047585,
                  15.14819
                ],
                [
                  81.059914,
                  16.55208
                ],
                [
                  81.384916,
                  17.721272
                ],
                [
                  80.569225,
                  19.514793
                ],
                [
                  78.217742,
                  20.06644
                ],
                [
                  77.179011,
                  18.556975
                ]
              ]
            ],
            "type": "Polygon"
          },
          "type": "Place",
          "address": "Telangana"
        },
        "itemStatus": "ACTIVE",
        "ownerUserId": "504f246c-4130-451f-b4df-ce41e245a754",
        "cos": "49f96c4c-e595-4fee-984c-43dededfba48",
        "itemCreatedAt": "2024-01-01T11:26:50+0530"
      },
      {
        "@context": "https://voc.iudx.org.in/",
        "id": "e5d6a8df-9def-4c88-897f-202a927663ef",
        "id_bck": "imd.gov.in/d7733b0c544dfb3137767e5efa2c1ccd3b069bf8/rs.adex.org.in/agromet-imd/district-codes",
        "type": [
          "adex:Resource",
          "adex:AgriAdvisory",
          "iudx:Resource",
          "iudx:AgriAdvisory"
        ],
        "name": "district-codes",
        "label": "District Codes for Agromet Advisory Data in Telangana State",
        "description": "Publishes district data information such as district code and district name for various districts and mandals (ASD) of Telangana state.",
        "tags": [
          "Advisory",
          "district",
          "crop",
          "district",
          "data",
          "code"
        ],
        "accessPolicy": "OPEN",
        "apdURL": "acl-apd.adex.org.in",
        "provider": "e0adf587-8210-406d-8c59-8c0f27e147af",
        "provider_bck": "imd.gov.in/d7733b0c544dfb3137767e5efa2c1ccd3b069bf8",
        "resourceServer": "41bb4389-ebaf-4df7-a575-556ec6092a25",
        "resourceGroup": "5d97f1bc-d548-4d02-9fd1-0e6d0f8227dd",
        "resourceGroup_bck": "imd.gov.in/d7733b0c544dfb3137767e5efa2c1ccd3b069bf8/rs.adex.org.in/agromet-imd",
        "resourceType": "DATASET",
        "adexResourceAPIs": [
          "ATTR"
        ],
        "iudxResourceAPIs": [
          "ATTR"
        ],
        "dataDescriptor": {
          "@context": "https://agrijson.org/",
          "type": [
            "iudx:DataDescriptor",
            "iudx:AgriAdvisory",
            "adex:DataDescriptor",
            "adex:AgriAdvisory"
          ],
          "dataDescriptorLabel": "Data descriptor for Agromet Advisory District Data Information for various district and mandals (ASD) in Telangana State",
          "description": "Data attribute details of agromet advisory district data information for various district and mandals (ASD) in Telangana State.",
          "districtCode": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "The district code corresponding to this observation.",
            "dataSchema": "iudx:Text"
          },
          "districtName": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "Name of the district corresponding to this observation.",
            "dataSchema": "iudx:Text"
          }
        },
        "dataSample": {
          "districtCode": "541",
          "districtName": "KHAMMAM"
        },
        "location": {
          "geometry": {
            "coordinates": [
              [
                [
                  77.179011,
                  18.556975
                ],
                [
                  77.047585,
                  15.14819
                ],
                [
                  81.059914,
                  16.55208
                ],
                [
                  81.384916,
                  17.721272
                ],
                [
                  80.569225,
                  19.514793
                ],
                [
                  78.217742,
                  20.06644
                ],
                [
                  77.179011,
                  18.556975
                ]
              ]
            ],
            "type": "Polygon"
          },
          "type": "Place",
          "address": "Telangana"
        },
        "itemStatus": "ACTIVE",
        "ownerUserId": "504f246c-4130-451f-b4df-ce41e245a754",
        "cos": "49f96c4c-e595-4fee-984c-43dededfba48",
        "itemCreatedAt": "2024-01-01T11:26:54+0530"
      },
      {
        "@context": "https://voc.iudx.org.in/",
        "id": "9c24f067-9552-45c2-9137-512263651b79",
        "id_bck": "tsmarketing.in/fb9a687092654eef990c3471ab50a5910fd08d12/rs.adex.org.in/telangana-amc-info/khammam-price-info",
        "type": [
          "adex:Resource",
          "adex:AgriMarket",
          "iudx:Resource",
          "iudx:AgriMarket"
        ],
        "name": "khammam-price-info",
        "label": "AMC Commodity Price Information in Khammam District",
        "description": "Publishes the price information of commodities in the Agricultural Market Committee (AMC) on a daily basis in Khammam district.",
        "tags": [
          "land",
          "crop",
          "commodity",
          "market",
          "price",
          "variety",
          "mandi",
          "district",
          "amc",
          "agency",
          "traders",
          "procurement",
          "khammam prices",
          "agricultural produce",
          "apmc"
        ],
        "accessPolicy": "SECURE",
        "apdURL": "acl-apd.adex.org.in",
        "provider": "6e70bb6d-43a2-4f0d-a79e-6c2ea1fa1382",
        "provider_bck": "tsmarketing.in/fb9a687092654eef990c3471ab50a5910fd08d12",
        "resourceServer": "41bb4389-ebaf-4df7-a575-556ec6092a25",
        "resourceGroup": "3f01f800-92d7-4ffa-afe3-7cb4fb8aa3ee",
        "resourceGroup_bck": "tsmarketing.in/fb9a687092654eef990c3471ab50a5910fd08d12/rs.adex.org.in/telangana-amc-info",
        "resourceType": "MESSAGESTREAM",
        "adexResourceAPIs": [
          "TEMPORAL",
          "ATTR"
        ],
        "iudxResourceAPIs": [
          "TEMPORAL",
          "ATTR"
        ],
        "dataDescriptor": {
          "@context": "https://agrijson.org/",
          "type": [
            "adex:DataDescriptor",
            "adex:AgriMarket",
            "iudx:Resource",
            "iudx:AgriMarket"
          ],
          "dataDescriptorLabel": "Data descriptor for the Commodity Price Information in the Agricultural Market Committee (AMC) in Khammam district.",
          "description": "Data attribute details of the Commodity Price Information in the Agricultural Market Committee (AMC) in Khammam district.",
          "amcName": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "The name of the AMC corresponding to this observation.",
            "dataSchema": "adex:Text"
          },
          "amcCode": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "The unique code assigned to the AMC corresponding to this observation.",
            "dataSchema": "adex:Text"
          },
          "commodityVarietyName": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "The name of the commodity's variety corresponding to this observation.",
            "dataSchema": "adex:Text"
          },
          "agencyName": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "The name of the procuring agency for a commodity in the AMC corresponding to this observation.",
            "dataSchema": "adex:Text"
          },
          "arrivalQuantity": {
            "type": [
              "ValueDescriptor"
            ],
            "dataSchema": "adex:Number",
            "unitCode": "DTN",
            "unitText": "decitonne",
            "description": "The quantity of commodity arrived at the AMC on the date corresponding to this observation."
          },
          "minimumPrice": {
            "type": [
              "ValueDescriptor"
            ],
            "dataSchema": "adex:Number",
            "unitCode": "INR",
            "unitText": "Indian Rupee",
            "description": "The minimum price of the commodity at the AMC corresponding to this observation."
          },
          "maximumPrice": {
            "type": [
              "ValueDescriptor"
            ],
            "dataSchema": "adex:Number",
            "unitCode": "INR",
            "unitText": "Indian Rupee",
            "description": "The maximum price of the commodity at the AMC corresponding to this observation."
          },
          "modalPrice": {
            "type": [
              "ValueDescriptor"
            ],
            "dataSchema": "adex:Number",
            "unitCode": "INR",
            "unitText": "Indian Rupee",
            "description": "The modal price of the commodity at the AMC corresponding to this observation."
          },
          "observationDateTime": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "Timestamp corresponding to this observation.",
            "dataSchema": "adex:DateTime"
          }
        },
        "dataSample": {
          "amcName": "Khammam",
          "commodityVarietyName": "Black Gram -Common",
          "arrivalQuantity": 13,
          "minimumPrice": 6350,
          "maximumPrice": 6700,
          "modalPrice": 6700,
          "agencyName": "Private Traders",
          "observationDateTime": "2023-02-02T00:00:00+05:30"
        },
        "location": {
          "type": "Place",
          "address": "Khammam, Telangana",
          "geometry": {
            "coordinates": [
              [
                [
                  80.148689,
                  17.305026
                ],
                [
                  80.091376,
                  17.248975
                ],
                [
                  80.154935,
                  17.190646
                ],
                [
                  80.200631,
                  17.220805
                ],
                [
                  80.200215,
                  17.279124
                ],
                [
                  80.148689,
                  17.305026
                ]
              ]
            ],
            "type": "Polygon"
          }
        },
        "itemStatus": "ACTIVE",
        "ownerUserId": "9ca1732c-232e-4686-b21e-a5a355c3e843",
        "cos": "49f96c4c-e595-4fee-984c-43dededfba48",
        "itemCreatedAt": "2024-01-01T11:07:39+0530"
      },
      {
        "@context": "https://voc.iudx.org.in/",
        "id": "537b3f73-c543-4b69-bc4e-5790ef54b6c3",
        "id_bck": "tsmarketing.in/fb9a687092654eef990c3471ab50a5910fd08d12/rs.adex.org.in/telangana-amc-info/amc-list",
        "type": [
          "adex:Resource",
          "adex:AgriMarket",
          "iudx:Resource",
          "iudx:AgriMarket"
        ],
        "name": "amc-list",
        "label": "List of AMCs in Telangana",
        "description": "Publishes information about the Agricultural Market Committees (AMCs) once in a month, that are available across Telangana State.",
        "tags": [
          "land",
          "crop",
          "commodity",
          "market",
          "price",
          "mandi",
          "variety",
          "district",
          "amc",
          "agency",
          "traders",
          "procurement",
          "amc list"
        ],
        "accessPolicy": "SECURE",
        "apdURL": "acl-apd.adex.org.in",
        "provider": "6e70bb6d-43a2-4f0d-a79e-6c2ea1fa1382",
        "provider_bck": "tsmarketing.in/fb9a687092654eef990c3471ab50a5910fd08d12",
        "resourceServer": "41bb4389-ebaf-4df7-a575-556ec6092a25",
        "resourceGroup": "3f01f800-92d7-4ffa-afe3-7cb4fb8aa3ee",
        "resourceGroup_bck": "tsmarketing.in/fb9a687092654eef990c3471ab50a5910fd08d12/rs.adex.org.in/telangana-amc-info",
        "resourceType": "MESSAGESTREAM",
        "adexResourceAPIs": [
          "TEMPORAL",
          "ATTR"
        ],
        "iudxResourceAPIs": [
          "TEMPORAL",
          "ATTR"
        ],
        "dataDescriptor": {
          "@context": "https://agrijson.org/",
          "type": [
            "adex:DataDescriptor",
            "adex:AgriMarket",
            "iudx:DataDescriptor",
            "iudx:AgriMarket"
          ],
          "dataDescriptorLabel": "Data descriptor for the list of Agricultural Market Committee (AMC) in Telangana State.",
          "description": "Data attribute details of the list of Agricultural Market Committee (AMC) in Telangana State.",
          "districtCode": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "The unique code associated to the district corresponding to this observation.",
            "dataSchema": "adex:Text"
          },
          "districtName": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "The name of the district at which the AMC is located.",
            "dataSchema": "adex:Text"
          },
          "address": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "Name of the area or locality in Telangana state at which the AMC is located.",
            "dataSchema": "adex:Text"
          },
          "amcCode": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "The unique code assigned to the AMC corresponding to this observation.",
            "dataSchema": "adex:Text"
          },
          "amcName": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "The name of the AMC corresponding to this observation.",
            "dataSchema": "adex:Text"
          },
          "amcGrade": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "The grading based on income of AMC such as 'selection', 'special', 'grade 1','grade 2', 'grade 3'.",
            "dataSchema": "adex:Text"
          },
          "phone": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "The contact number for the AMC corresponding to this observation.",
            "dataSchema": "adex:Text"
          },
          "observationDateTime": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "Last reported time of observation.",
            "dataSchema": "adex:DateTime"
          }
        },
        "dataSample": {
          "districtCode": "14",
          "districtName": "Mahbubnagar",
          "address": "OC-w",
          "amcCode": "300",
          "amcName": "Badepally",
          "amcGrade": "Spl.Gr",
          "phone": "7330733263",
          "observationDateTime": "2023-04-10T11:43:13+05:30"
        },
        "location": {
          "type": "Place",
          "address": "Telangana",
          "geometry": {
            "coordinates": [
              [
                [
                  78.196385,
                  19.955661
                ],
                [
                  76.396029,
                  17.128178
                ],
                [
                  78.235175,
                  15.1213
                ],
                [
                  81.445091,
                  17.179754
                ],
                [
                  80.601397,
                  19.416946
                ],
                [
                  78.196385,
                  19.955661
                ]
              ]
            ],
            "type": "Polygon"
          }
        },
        "itemStatus": "ACTIVE",
        "ownerUserId": "9ca1732c-232e-4686-b21e-a5a355c3e843",
        "cos": "49f96c4c-e595-4fee-984c-43dededfba48",
        "itemCreatedAt": "2024-01-01T11:07:42+0530"
      },
      {
        "@context": "https://voc.iudx.org.in/",
        "id": "938f7c21-5a53-4d5e-988b-60d8f2e0c963",
        "id_bck": "krishitantra.com/dd9561b09f5d63b59160388f96085a55d24e7795/gateway.adex.org.in/krishitantra-data/soil-tests-data",
        "type": [
          "adex:Resource",
          "adex:SoilHealth",
          "iudx:Resource",
          "iudx:SoilHealth"
        ],
        "name": "soil-tests-data",
        "label": "Soil Test Results for CropLands in Telangana State from KrishiTantra",
        "description": "Publishes information of soil test results of cropland in Telangana state from KrishiTantra",
        "tags": [
          "krishitantra",
          "variety",
          "crop",
          "commodity",
          "market",
          "village",
          "land",
          "crop",
          "crop type",
          "irrigation",
          "area sown",
          "land details",
          "soil test",
          "survey number"
        ],
        "accessPolicy": "SECURE",
        "apdURL": "acl-apd.adex.org.in",
        "provider": "a284e308-41ef-4ca6-9064-6ab5c247ab3c",
        "provider_bck": "krishitantra.com/dd9561b09f5d63b59160388f96085a55d24e7795",
        "resourceServer": "41bb4389-ebaf-4df7-a575-556ec6092a25",
        "resourceGroup": "e59365a9-7808-450d-8a42-3269dfcd7e8b",
        "resourceGroup_bck": "krishitantra.com/dd9561b09f5d63b59160388f96085a55d24e7795/gateway.adex.org.in/krishitantra-data",
        "resourceType": "MESSAGESTREAM",
        "adexResourceAPIs": [
          "SPATIAL",
          "ATTR",
          "TEMPORAL"
        ],
        "iudxResourceAPIs": [
          "SPATIAL",
          "ATTR",
          "TEMPORAL"
        ],
        "dataDescriptor": {
          "@context": "https://agrijson.adex.org.in/",
          "type": [
            "iudx:DataDescriptor",
            "iudx:SoilHealth",
            "adex:DataDescriptor",
            "adex:SoilHealth"
          ],
          "dataDescriptorLabel": "Data Descriptor Of Soil Test Results for Cropland in Telangana State from KrishiTantra",
          "description": "Data attribute details of soil test results of cropland and the crops that are sown in the agricultural land of Telangana State from KrishiTantra.",
          "sampleID": {
            "description": "The unique ID representing the sample corresponding to this observation",
            "dataSchema": "adex:Text",
            "type": [
              "ValueDescriptor"
            ]
          },
          "location": {
            "description": "Physical coordinates of cropland corresponding to this observation.",
            "dataSchema": "adex:Point",
            "type": [
              "ValueDescriptor"
            ]
          },
          "cropNameCommon": {
            "description": "The common/local name of the crop species corresponding to the observation.",
            "dataSchema": "adex:Text",
            "type": [
              "ValueDescriptor"
            ]
          },
          "previousCropName": {
            "description": "The name of the crop that was cultivated prior to the current crop in the land/ soil corresponding to this observation.",
            "dataSchema": "adex:Text",
            "type": [
              "ValueDescriptor"
            ]
          },
          "previousYield": {
            "description": "The amount of yield produced by the crop that was cultivated prior to the current crop in the land/ soil corresponding to this observation.",
            "dataSchema": "adex:Number",
            "type": [
              "ValueDescriptor"
            ]
          },
          "targetYield": {
            "description": "The desired or expected level of production for a specific agricultural crop within a given area or field.",
            "dataSchema": "adex:Number",
            "type": [
              "ValueDescriptor"
            ]
          },
          "surveyNumber": {
            "description": "The unique land survey number allocated to the land corresponding to this observation.",
            "dataSchema": "adex:Text",
            "type": [
              "ValueDescriptor"
            ]
          },
          "boron": {
            "description": "Observed value of Boron composition in the soil.",
            "dataSchema": "adex:Number",
            "type": [
              "ValueDescriptor"
            ],
            "unitCode": "NA",
            "unitText": "milligram per kilogram mg/kg"
          },
          "cu": {
            "description": "Observed value of Copper composition in the soil.",
            "dataSchema": "adex:Number",
            "type": [
              "ValueDescriptor"
            ],
            "unitCode": "NA",
            "unitText": "milligram per kilogram mg/kg"
          },
          "electricalConductivity": {
            "description": "The measure of electrical conductivity of the entity corresponding to this observation.",
            "dataSchema": "adex:Text",
            "type": [
              "ValueDescriptor"
            ],
            "unitText": "decisiemens per meter [dS/m]"
          },
          "fe": {
            "description": "Observed value of Iron composition in the soil.",
            "dataSchema": "adex:Number",
            "type": [
              "ValueDescriptor"
            ],
            "unitCode": "NA",
            "unitText": "milligram per kilogram mg/kg"
          },
          "organicCarbon": {
            "description": "Observed value of Organic Carbon composition in the soil.",
            "dataSchema": "adex:Number",
            "type": [
              "ValueDescriptor"
            ],
            "unitText": "weighted %"
          },
          "sulphur": {
            "description": "Observed value of sulpur composition in the soil.",
            "dataSchema": "adex:Number",
            "type": [
              "ValueDescriptor"
            ],
            "unitCode": "NA",
            "unitText": "milligram per kilogram mg/kg"
          },
          "zn": {
            "description": "Observed value of Zinc composition in the soil.",
            "dataSchema": "adex:Number",
            "type": [
              "ValueDescriptor"
            ],
            "unitCode": "NA",
            "unitText": "milligram per kilogram mg/kg"
          },
          "potassium": {
            "description": "Observed value of Potassium composition in the soil.",
            "dataSchema": "adex:Number",
            "type": [
              "ValueDescriptor"
            ],
            "unitText": "kilogram per hectare [kg/hectare]"
          },
          "nitrogen": {
            "description": "Observed value of Nitrogen composition in the soil.",
            "dataSchema": "adex:Number",
            "type": [
              "ValueDescriptor"
            ],
            "unitText": "kilogram per hectare [kg/hectare]"
          },
          "phosphorus": {
            "description": "Observed value of Phosphorus composition in the soil.",
            "dataSchema": "adex:Number",
            "type": [
              "ValueDescriptor"
            ],
            "unitText": "kilogram per hectare [kg/hectare]"
          },
          "pH": {
            "description": "The measure of the acidity or basicity.",
            "dataSchema": "adex:Number",
            "type": [
              "ValueDescriptor"
            ],
            "unitCode": "C62",
            "unitText": "dimensionless"
          },
          "testCentreID": {
            "description": "The unique ID of the centre at which the sample is being tested.",
            "dataSchema": "adex:Text",
            "type": [
              "ValueDescriptor"
            ]
          },
          "testCentreName": {
            "description": "The name of the centre at which the sample is being tested.",
            "dataSchema": "adex:Text",
            "type": [
              "ValueDescriptor"
            ]
          },
          "testCentreCode": {
            "description": "The unique code of the centre at which the sample is being tested.",
            "dataSchema": "adex:Text",
            "type": [
              "ValueDescriptor"
            ]
          },
          "testDateTime": {
            "description": "The date and time at which the sample is being tested in the laboratory or the testing centre.",
            "dataSchema": "adex:DateTime",
            "type": [
              "ValueDescriptor"
            ]
          },
          "observationDateTime": {
            "description": "Last reported time of observation.",
            "dataSchema": "adex:DateTime",
            "type": [
              "ValueDescriptor"
            ]
          }
        },
        "dataSample": {
          "sampleID": "62bc08ff2582d0001b3398f4",
          "location": {
            "type": "Polygon",
            "coordinates": [
              [
                [
                  79.95679,
                  17.2155923
                ],
                [
                  79.95655383914708,
                  17.215780724299044
                ],
                [
                  79.95632819831371,
                  17.215754143156172
                ],
                [
                  79.95643950998783,
                  17.21564493625198
                ],
                [
                  79.95668392628431,
                  17.21551907601551
                ],
                [
                  79.95679,
                  17.2155923
                ]
              ]
            ]
          },
          "cropNameCommon": "chilli (irrigated)",
          "previousCropName": "chilli (irrigated)",
          "previousYield": 20000,
          "targetYield": 40000,
          "surveyNumber": "462",
          "boron": 0.22,
          "cu": 0.13,
          "electricalConductivity": 0.5,
          "fe": 3.86,
          "organicCarbon": 0.78,
          "sulphur": 12.6,
          "zn": 0.76,
          "potassium": 155,
          "nitrogen": None,
          "phosphorus": 20.1,
          "pH": 8.07,
          "testCentreID": "6296fe392bca3f0013a31f9e",
          "testCentreName": "Raithu Vedika",
          "testCentreCode": "digitalgreen00001",
          "testDateTime": "2022-07-03T13:53:30+05:30",
          "observationDateTime": "2022-06-29T08:10:39+05:30"
        },
        "location": {
          "geometry": {
            "coordinates": [
              [
                [
                  77.179011,
                  18.556975
                ],
                [
                  77.047585,
                  15.14819
                ],
                [
                  81.059914,
                  16.55208
                ],
                [
                  81.384916,
                  17.721272
                ],
                [
                  80.569225,
                  19.514793
                ],
                [
                  78.217742,
                  20.06644
                ],
                [
                  77.179011,
                  18.556975
                ]
              ]
            ],
            "type": "Polygon"
          },
          "type": "Place",
          "address": "Telangana"
        },
        "itemStatus": "ACTIVE",
        "ownerUserId": "05c58686-4d2c-436c-a06b-1fb8b6299b55",
        "cos": "49f96c4c-e595-4fee-984c-43dededfba48",
        "itemCreatedAt": "2024-01-02T01:15:05+0530"
      },
      {
        "@context": "https://voc.iudx.org.in/",
        "id": "d60e022f-e32a-4d66-8178-0e7d91361c95",
        "type": [
          "iudx:Resource",
          "iudx:Weather",
          "adex:Resource",
          "adex:Weather"
        ],
        "name": "telangana-weather-info",
        "label": "Niruthi Weather Information for Telangana",
        "description": "Publishes information about weather parameters such as solar radiation, temperature, humidity etc., on a daily basis (7 days prior to the current day), observed over the various villages of Telangana state, as provided by Niruthi organization.",
        "tags": [
          "environment",
          "weather",
          "weather monitoring sensors",
          "rainfall",
          "precipitation",
          "weather information",
          "humidity",
          "weather forecast",
          "meteorological department",
          "temperature",
          "imd",
          "niruthi"
        ],
        "accessPolicy": "SECURE",
        "apdURL": "acl-apd.adex.org.in",
        "provider": "fdb2bc10-6dbb-4844-9f0f-4a343a870f61",
        "resourceServer": "41bb4389-ebaf-4df7-a575-556ec6092a25",
        "resourceGroup": "e4917519-c5fc-4bd9-9f89-0dd22aa54eec",
        "resourceType": "MESSAGESTREAM",
        "adexResourceAPIs": [
          "TEMPORAL",
          "ATTR"
        ],
        "iudxResourceAPIs": [
          "TEMPORAL",
          "ATTR"
        ],
        "dataDescriptor": {
          "@context": "https://agrijson.adex.org/",
          "type": [
            "iudx:DataDescriptor",
            "iudx:Weather",
            "adex:DataDescriptor",
            "adex:Weather"
          ],
          "dataDescriptorLabel": "Data descriptor for weather information in Telangana district",
          "description": "Data attribute details of weather monitoring system in Telangana district.",
          "subdistrictName": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "Name of the subdistrict or mandal corresponding to this observation.",
            "dataSchema": "adex:Text"
          },
          "villageName": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "Name of the village corresponding to this observation.",
            "dataSchema": "adex:Text"
          },
          "gramPanchayatName": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "Name of the gram panchayat corresponding to this observation.",
            "dataSchema": "adex:Text"
          },
          "windSpeed": {
            "type": [
              "TimeSeriesAggregation"
            ],
            "description": "Describes the aggregated value of wind speed corresponding to this observation.",
            "maxOverTime": {
              "description": "The maximum value of wind speed over a period of 24 hours.",
              "unitCode": "MTS",
              "unitText": "metre per second",
              "dataSchema": "adex:Number",
              "type": [
                "ValueDescriptor"
              ]
            },
            "minOverTime": {
              "description": "The minimum value of wind speed over a period of 24 hours.",
              "unitCode": "MTS",
              "unitText": "metre per second",
              "dataSchema": "adex:Number",
              "type": [
                "ValueDescriptor"
              ]
            }
          },
          "precipitation": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "The total amount of precipitation/rainfall over a period of 24 hours.",
            "unitCode": "MMT",
            "unitText": "millimetre",
            "dataSchema": "adex:Number"
          },
          "relativeHumidity": {
            "type": [
              "TimeSeriesAggregation"
            ],
            "description": "The aggregated values for humidity (water vapour in air) over a period of 24 hours.",
            "avgOverTime": {
              "type": [
                "ValueDescriptor"
              ],
              "description": "The average value of relative humidity over a period of 24 hours",
              "dataSchema": "adex:Number",
              "unitCode": "P1",
              "unitText": "percent"
            },
            "maxOverTime": {
              "type": [
                "ValueDescriptor"
              ],
              "description": "The maximum value of relative humidity over a period of 24 hours",
              "dataSchema": "adex:Number",
              "unitCode": "P1",
              "unitText": "percent"
            },
            "minOverTime": {
              "type": [
                "ValueDescriptor"
              ],
              "description": "The minimum value of of relative humidity over a period of 24 hours",
              "dataSchema": "adex:Number",
              "unitCode": "P1",
              "unitText": "percent"
            }
          },
          "solarRadiation": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "The total amount of solar radiation over a period of 24 hours.",
            "unitText": "megajoule per day",
            "dataSchema": "adex:Number"
          },
          "dewPoint": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "The observed dew point temperature over a period of 24 hours.",
            "unitCode": "CEL",
            "unitText": "degree Celsius",
            "dataSchema": "adex:Number"
          },
          "airTemperature": {
            "type": [
              "TimeSeriesAggregation"
            ],
            "description": "Describes the aggregated value for air temperature corresponding to this observation.",
            "maxOverTime": {
              "description": "The maximum value of air temperature over a period of 24 hours.",
              "unitCode": "CEL",
              "unitText": "degree Celsius",
              "dataSchema": "adex:Number",
              "type": [
                "ValueDescriptor"
              ]
            },
            "minOverTime": {
              "description": "The minimum value of air temperature over a period of 24 hours.",
              "unitCode": "CEL",
              "unitText": "degree Celsius",
              "dataSchema": "adex:Number",
              "type": [
                "ValueDescriptor"
              ]
            }
          },
          "dayLength": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "The total time period of sunlight over a period of 24 hours.",
            "unitCode": "HUR",
            "unitText": "hour",
            "dataSchema": "adex:Number"
          },
          "location": {
            "description": "The physical coordinates of the location at which the weather details corresponding to this observation has been captured.",
            "type": [
              "ValueDescriptor"
            ],
            "dataSchema": "iudx:Point"
          },
          "observationDateTime": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "Represents the day for which the 24 hour period aggregations of the weather parameters correspond to this observation.",
            "dataSchema": "adex:DateTime"
          }
        },
        "dataSample": {
          "subdistrictName": "Sathupalle",
          "gramPanchayatName": "RUDRAKSHAPALLI",
          "villageName": "Bacharam",
          "windSpeed": {
            "avgOverTime": 3.12,
            "maxOverTime": 5.64
          },
          "precipitation": 8.14,
          "relativeHumidity": {
            "avgOverTime": 47.59,
            "maxOverTime": 81.77,
            "minOverTime": 39.13
          },
          "solarRadiation": 15.27,
          "dewPoint": 23.04,
          "airTemperature": {
            "maxOverTime": 39.51,
            "minOverTime": 26.41
          },
          "dayLength": 5.14,
          "location": {
            "type": "Point",
            "coordinates": [
              80.81,
              17.26
            ]
          },
          "observationDateTime": "2023-07-24T18:52:04+05:30"
        },
        "location": {
          "geometry": {
            "coordinates": [
              [
                [
                  77.179011,
                  18.556975
                ],
                [
                  77.047585,
                  15.14819
                ],
                [
                  81.059914,
                  16.55208
                ],
                [
                  81.384916,
                  17.721272
                ],
                [
                  80.569225,
                  19.514793
                ],
                [
                  78.217742,
                  20.06644
                ],
                [
                  77.179011,
                  18.556975
                ]
              ]
            ],
            "type": "Polygon"
          },
          "type": "Place",
          "address": "Telangana"
        },
        "itemStatus": "ACTIVE",
        "ownerUserId": "f738f38a-7fde-478b-9650-4187603dec45",
        "cos": "49f96c4c-e595-4fee-984c-43dededfba48",
        "itemCreatedAt": "2024-01-02T11:37:25+0530"
      },
      {
        "@context": "https://voc.iudx.org.in/",
        "id": "b72a23b8-5767-48a1-8fc8-6abafe23e69a",
        "id_bck": "tsdps.telangana.gov.in/b1c9bd3e24bc3db7cbaef607e3907a02133208ba/rs.adex.org.in/khammam-env-weather/subdistrict-weather-info",
        "type": [
          "iudx:Resource",
          "iudx:Weather",
          "adex:Resource",
          "adex:Weather"
        ],
        "name": "subdistrict-weather-info",
        "label": "Weather Information in Khammam District",
        "description": "Publishes information about weather parameters such as precipitation, temperature, humidity etc. for the last 24 hours on daily basis, observed over the mandals of Khammam district.",
        "tags": [
          "environment",
          "weather",
          "weather monitoring sensors",
          "rainfall",
          "precipitation",
          "weather information",
          "humidity",
          "weather forecast",
          "meteorological department",
          "temperature"
        ],
        "accessPolicy": "SECURE",
        "apdURL": "acl-apd.adex.org.in",
        "provider": "efa475a7-9ca2-4832-99c9-33269071fa01",
        "provider_bck": "tsdps.telangana.gov.in/b1c9bd3e24bc3db7cbaef607e3907a02133208ba",
        "resourceServer": "41bb4389-ebaf-4df7-a575-556ec6092a25",
        "resourceGroup": "f5d4d767-dfdd-48b0-8afc-aa49da4c9776",
        "resourceGroup_bck": "tsdps.telangana.gov.in/b1c9bd3e24bc3db7cbaef607e3907a02133208ba/rs.adex.org.in/khammam-env-weather",
        "resourceType": "MESSAGESTREAM",
        "adexResourceAPIs": [
          "TEMPORAL",
          "ATTR"
        ],
        "iudxResourceAPIs": [
          "TEMPORAL",
          "ATTR"
        ],
        "dataDescriptor": {
          "@context": "https://agrijson.org/",
          "type": [
            "iudx:DataDescriptor",
            "iudx:Weather",
            "adex:DataDescriptor",
            "adex:Weather"
          ],
          "dataDescriptorLabel": "Data descriptor for weather information in Khammam district",
          "description": "Data attribute details of weather monitoring system in Khammam district.",
          "districtCode": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "The unique code associated to the district corresponding to this observation.",
            "dataSchema": "adex:Text"
          },
          "subdistrictCode": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "The unique code assigned to the subdistrict or mandal corresponding to this observation.",
            "dataSchema": "adex:Text"
          },
          "subdistrictName": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "Name of the subdistrict or mandal corresponding to this observation.",
            "dataSchema": "adex:Text"
          },
          "precipitation": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "Cumulative values of precipitation/rainfall for the last 24 hours (from yesterday 8-30 AM to today 8-30 AM).",
            "unitCode": "MMT",
            "unitText": "millimetre (mm)",
            "dataSchema": "adex:Number"
          },
          "airTemperature": {
            "type": [
              "TimeSeriesAggregation"
            ],
            "description": "The aggregated value for air temperature in degree Celsius over the last 24 hours (from yesterday 8-30 AM to today 8-30 AM).",
            "maxOverTime": {
              "type": [
                "ValueDescriptor"
              ],
              "description": "Maximum value of air temperature over the last 24 hours",
              "dataSchema": "adex:Number",
              "unitCode": "CEL",
              "unitText": "degree Celsius (C)"
            },
            "minOverTime": {
              "type": [
                "ValueDescriptor"
              ],
              "description": "Minimum value of air temperature over the last 24 hours",
              "dataSchema": "adex:Number",
              "unitCode": "CEL",
              "unitText": "degree Celsius (C)"
            }
          },
          "relativeHumidity": {
            "type": [
              "TimeSeriesAggregation"
            ],
            "description": "The aggregated values for humidity (water vapour in air) over the last 24 hours (from yesterday 8-30 AM to today 8-30 AM).",
            "maxOverTime": {
              "type": [
                "ValueDescriptor"
              ],
              "description": "Maximum value of relative humidity over the last 24 hours",
              "dataSchema": "adex:Number",
              "unitCode": "P1",
              "unitText": "percent"
            },
            "minOverTime": {
              "type": [
                "ValueDescriptor"
              ],
              "description": "Minimum value of of relative humidity over the last 24 hours",
              "dataSchema": "adex:Number",
              "unitCode": "P1",
              "unitText": "percent"
            }
          },
          "observationDateTime": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "Last reported time of observation.",
            "dataSchema": "adex:DateTime"
          }
        },
        "dataSample": {
          "districtCode": "31",
          "subdistrictCode": "6",
          "subdistrictName": "Kusumanchi",
          "precipitation": 0,
          "airTemperature": {
            "maxOverTime": 32.6,
            "minOverTime": 15.8
          },
          "relativeHumidity": {
            "maxOverTime": 80.3,
            "minOverTime": 28.4
          },
          "observationDateTime": "2023-02-03T08:30:00+05:30"
        },
        "location": {
          "type": "Place",
          "address": "Khammam, Telangana",
          "geometry": {
            "coordinates": [
              [
                [
                  80.148689,
                  17.305026
                ],
                [
                  80.091376,
                  17.248975
                ],
                [
                  80.154935,
                  17.190646
                ],
                [
                  80.200631,
                  17.220805
                ],
                [
                  80.200215,
                  17.279124
                ],
                [
                  80.148689,
                  17.305026
                ]
              ]
            ],
            "type": "Polygon"
          }
        },
        "itemStatus": "ACTIVE",
        "ownerUserId": "21aebe6e-e843-47b8-9018-d402c5acbbba",
        "cos": "49f96c4c-e595-4fee-984c-43dededfba48",
        "itemCreatedAt": "2024-01-01T11:27:53+0530"
      },
      {
        "@context": "https://voc.iudx.org.in/",
        "id": "0dc68957-c82c-4b1c-9c8a-c53c165cd705",
        "id_bck": "tsdps.telangana.gov.in/b1c9bd3e24bc3db7cbaef607e3907a02133208ba/rs.adex.org.in/khammam-env-weather/rainfall-history-info",
        "type": [
          "iudx:Resource",
          "iudx:Weather",
          "adex:Resource",
          "adex:Weather"
        ],
        "name": "rainfall-history-info",
        "label": "Historical Rainfall Information in Khammam District",
        "description": "Historical information of precipitation observed over the mandals in Khammam district.",
        "tags": [
          "environment",
          "weather",
          "weather monitoring sensors",
          "rainfall",
          "precipitation",
          "weather information",
          "weather forecast",
          "meteorological department",
          "subdistricts"
        ],
        "accessPolicy": "SECURE",
        "apdURL": "acl-apd.adex.org.in",
        "provider": "efa475a7-9ca2-4832-99c9-33269071fa01",
        "provider_bck": "tsdps.telangana.gov.in/b1c9bd3e24bc3db7cbaef607e3907a02133208ba",
        "resourceServer": "41bb4389-ebaf-4df7-a575-556ec6092a25",
        "resourceGroup": "f5d4d767-dfdd-48b0-8afc-aa49da4c9776",
        "resourceGroup_bck": "tsdps.telangana.gov.in/b1c9bd3e24bc3db7cbaef607e3907a02133208ba/rs.adex.org.in/khammam-env-weather",
        "resourceType": "MESSAGESTREAM",
        "adexResourceAPIs": [
          "TEMPORAL",
          "ATTR"
        ],
        "iudxResourceAPIs": [
          "TEMPORAL",
          "ATTR"
        ],
        "dataDescriptor": {
          "@context": "https://agrijson.org/",
          "type": [
            "iudx:DataDescriptor",
            "iudx:Weather",
            "adex:DataDescriptor",
            "adex:Weather"
          ],
          "dataDescriptorLabel": "Data descriptor for historical rainfall information in Khammam district",
          "description": "Data attribute details of rainfall monitoring system in Khammam district.",
          "districtCode": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "The unique code associated to the district corresponding to this observation.",
            "dataSchema": "adex:Text"
          },
          "subdistrictCode": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "The unique code assigned to the sub-district or mandal corresponding to this observation.",
            "dataSchema": "adex:Text"
          },
          "precipitation": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "Cumulative values of precipitation/rainfall for the last 24 hours (from yesterday 8-30 AM to today 8-30 AM).",
            "unitCode": "MMT",
            "unitText": "millimetre (mm)",
            "dataSchema": "adex:Number"
          },
          "subdistrictName": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "Name of the subdistrict or mandal corresponding to this observation.",
            "dataSchema": "adex:Text"
          },
          "observationDateTime": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "Last reported time of observation.",
            "dataSchema": "adex:DateTime"
          }
        },
        "dataSample": {
          "districtCode": "31",
          "subdistrictCode": "19",
          "subdistrictName": "Bonakal",
          "precipitation": 0,
          "observationDateTime": "2023-02-03T00:00:00+05:30"
        },
        "location": {
          "type": "Place",
          "address": "Khammam, Telangana",
          "geometry": {
            "coordinates": [
              [
                [
                  80.148689,
                  17.305026
                ],
                [
                  80.091376,
                  17.248975
                ],
                [
                  80.154935,
                  17.190646
                ],
                [
                  80.200631,
                  17.220805
                ],
                [
                  80.200215,
                  17.279124
                ],
                [
                  80.148689,
                  17.305026
                ]
              ]
            ],
            "type": "Polygon"
          }
        },
        "itemStatus": "ACTIVE",
        "ownerUserId": "21aebe6e-e843-47b8-9018-d402c5acbbba",
        "cos": "49f96c4c-e595-4fee-984c-43dededfba48",
        "itemCreatedAt": "2024-01-01T11:27:56+0530"
      },
      {
        "@context": "https://voc.iudx.org.in/",
        "id": "4aef701f-bf08-4f66-b38b-594a9c8c15cf",
        "id_bck": "tsmarketing.in/fb9a687092654eef990c3471ab50a5910fd08d12/rs.adex.org.in/telangana-amc-info/daily-price-info",
        "type": [
          "adex:Resource",
          "adex:AgriMarket",
          "iudx:Resource",
          "iudx:AgriMarket"
        ],
        "name": "daily-price-info",
        "label": "AMC Commodity Price Information in Telangana State",
        "description": "Publishes information about day-wise prices of the commodities in the Agricultural Market Committee (AMC) in Telangana State.",
        "tags": [
          "land",
          "crop",
          "commodity",
          "market",
          "price",
          "mandi",
          "variety",
          "district",
          "amc",
          "agency",
          "traders",
          "procurement",
          "apmc",
          "agricultural produce",
          "daily prices"
        ],
        "accessPolicy": "SECURE",
        "apdURL": "acl-apd.adex.org.in",
        "provider": "6e70bb6d-43a2-4f0d-a79e-6c2ea1fa1382",
        "provider_bck": "tsmarketing.in/fb9a687092654eef990c3471ab50a5910fd08d12",
        "resourceServer": "41bb4389-ebaf-4df7-a575-556ec6092a25",
        "resourceGroup": "3f01f800-92d7-4ffa-afe3-7cb4fb8aa3ee",
        "resourceGroup_bck": "tsmarketing.in/fb9a687092654eef990c3471ab50a5910fd08d12/rs.adex.org.in/telangana-amc-info",
        "resourceType": "MESSAGESTREAM",
        "adexResourceAPIs": [
          "TEMPORAL",
          "ATTR"
        ],
        "iudxResourceAPIs": [
          "TEMPORAL",
          "ATTR"
        ],
        "dataDescriptor": {
          "@context": "https://agrijson.org/",
          "type": [
            "adex:DataDescriptor",
            "adex:AgriMarket",
            "iudx:DataDescriptor",
            "iudx:AgriMarket"
          ],
          "dataDescriptorLabel": "Data descriptor for the Commodity Price Information at the Agricultural Market Committee (AMC) in Telangana State.",
          "description": "Data attribute details of the commodity price information at the Agricultural Market Committee (AMC) in Telangana State.",
          "amcName": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "The name of the AMC corresponding to this observation.",
            "dataSchema": "adex:Text"
          },
          "amcCode": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "The unique code assigned to the AMC corresponding to this observation.",
            "dataSchema": "adex:Text"
          },
          "marketID": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "The unique code assigned to the mandi corresponding to this observation.",
            "dataSchema": "adex:Text"
          },
          "marketName": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "The name of the mandi corresponding to this observation.",
            "dataSchema": "adex:Text"
          },
          "commodityVarietyName": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "The name of the commodity corresponding to this observation.",
            "dataSchema": "adex:Text"
          },
          "commodityVarietyCode": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "The unique code assigned to the commodity corresponding to this observation.",
            "dataSchema": "adex:Text"
          },
          "seedVarietyName": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "The name of the commodity's variety corresponding to this observation.",
            "dataSchema": "adex:Text"
          },
          "seedVarietyCode": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "The unique code assigned to the commodity's variety corresponding to this observation.",
            "dataSchema": "adex:Text"
          },
          "arrivalQuantity": {
            "type": [
              "ValueDescriptor"
            ],
            "dataSchema": "adex:Number",
            "unitCode": "DTN",
            "unitText": "decitonne",
            "description": "The quantity of commodity arrived at the AMC on the date corresponding to this observation."
          },
          "minimumPrice": {
            "type": [
              "ValueDescriptor"
            ],
            "dataSchema": "adex:Number",
            "unitCode": "INR",
            "unitText": "Indian Rupee",
            "description": "The minimum price of the commodity at the AMC corresponding to this observation."
          },
          "maximumPrice": {
            "type": [
              "ValueDescriptor"
            ],
            "dataSchema": "adex:Number",
            "unitCode": "INR",
            "unitText": "Indian Rupee",
            "description": "The maximum price of the commodity at the AMC corresponding to this observation."
          },
          "modalPrice": {
            "type": [
              "ValueDescriptor"
            ],
            "dataSchema": "adex:Number",
            "unitCode": "INR",
            "unitText": "Indian Rupee",
            "description": "The modal price of the commodity at the AMC corresponding to this observation."
          },
          "agencyName": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "The name of the procuring agency for a commodity in the AMC corresponding to this observation.",
            "dataSchema": "adex:Text"
          },
          "progArrivals": {
            "type": [
              "ValueDescriptor"
            ],
            "dataSchema": "adex:Number",
            "unitCode": "DTN",
            "unitText": "decitonne",
            "description": "The progressive arrival quantity of the commodity from 1st April of the current FY to the current date corresponding to this observation."
          },
          "marketValuation": {
            "type": [
              "ValueDescriptor"
            ],
            "dataSchema": "adex:Number",
            "unitCode": "INR",
            "unitText": "Indian Rupee",
            "description": "The modal price for the total quantity of the commodity arrived at the AMC (modalPrice x arrivalQuantity) corresponding to this observation."
          },
          "marketFee": {
            "type": [
              "ValueDescriptor"
            ],
            "dataSchema": "adex:Number",
            "unitCode": "INR",
            "unitText": "Indian Rupee",
            "description": "The AMC charges paid for the trade corresponding to this observation."
          },
          "observationDateTime": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "Timestamp corresponding to this observation.",
            "dataSchema": "adex:DateTime"
          }
        },
        "dataSample": {
          "amcName": "Warangal",
          "amcCode": "246",
          "marketName": "Warangal",
          "marketID": "886",
          "commodityVarietyName": "Water Melon",
          "commodityVarietyCode": "86",
          "seedVarietyName": "Common",
          "seedVarietyCode": "86",
          "arrivalQuantity": 120.0,
          "minimumPrice": 400.0,
          "maximumPrice": 1000.0,
          "modalPrice": 670.0,
          "marketFee": 0.0,
          "agencyName": "Private Traders",
          "marketValuation": 0.0,
          "observationDateTime": "2023-04-11T00:00:00+05:30"
        },
        "location": {
          "type": "Place",
          "address": "Telangana",
          "geometry": {
            "coordinates": [
              [
                [
                  78.196385,
                  19.955661
                ],
                [
                  76.396029,
                  17.128178
                ],
                [
                  78.235175,
                  15.1213
                ],
                [
                  81.445091,
                  17.179754
                ],
                [
                  80.601397,
                  19.416946
                ],
                [
                  78.196385,
                  19.955661
                ]
              ]
            ],
            "type": "Polygon"
          }
        },
        "itemStatus": "ACTIVE",
        "ownerUserId": "9ca1732c-232e-4686-b21e-a5a355c3e843",
        "cos": "49f96c4c-e595-4fee-984c-43dededfba48",
        "itemCreatedAt": "2024-01-02T01:22:26+0530"
      },
      {
        "@context": "https://voc.iudx.org.in/",
        "id": "c5422a0f-e60f-48e4-9d1e-1fa4b1714900",
        "type": [
          "adex:Resource",
          "adex:Farmer",
          "iudx:Resource",
          "iudx:Farmer"
        ],
        "name": "get-farmer-crop-data",
        "label": "Crop and Cropland Information for Farmer Pattadar PassBook(PPB) Numbers in Telangana State",
        "description": "Publishes information of farmers such as name, mobile number and the crops that are sown in the agricultural land of the Telangana State.",
        "tags": [
          "land",
          "crop",
          "crop type",
          "district",
          "irrigation",
          "area sown",
          "land details",
          "farmer details",
          "village",
          "revenue information",
          "pattadar passbook number",
          "ppb"
        ],
        "accessPolicy": "PII",
        "apdURL": "consent.ts.adex.org.in",
        "provider": "52bdfa1a-bd65-4b20-822b-a5a55d839394",
        "resourceServer": "948f45cc-5f0a-4cea-b602-f634917a9d65",
        "resourceGroup": "0b054426-a1d2-4b0e-96e2-62e53e0f21e9",
        "resourceType": "MESSAGESTREAM",
        "adexResourceAPIs": [
          "ATTR",
          "TEMPORAL"
        ],
        "iudxResourceAPIs": [
          "ATTR",
          "TEMPORAL"
        ],
        "dataDescriptor": {
          "@context": "https://agrijson.org/",
          "type": [
            "iudx:DataDescriptor",
            "iudx:Farmer",
            "adex:DataDescriptor",
            "adex:Farmer"
          ],
          "dataDescriptorLabel": "Data descriptor for Crop and Cropland info as per Pattadar Passbook Number in Telangana State",
          "description": "Data attribute details of crop and cropland information for farmer pattadar passBook(PPB) numbers in Telangana State.",
          "name": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "Name of the farmer corresponding to this observation.",
            "dataSchema": "adex:Text"
          },
          "phone": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "Mobile number of the farmer corresponding to this observation.",
            "dataSchema": "adex:Number",
            "unitCode": "C62",
            "unitText": "Dimensionless"
          },
          "year": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "The financial year in which the crop is cultivated corresponding to this observation.",
            "dataSchema": "iudx:Number",
            "unitCode": "C62",
            "unitText": "Dimensionless"
          },
          "cropSeason": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "Season of the Agricultural year in which the crop corresponding to this observation was grown. There are three seasons represented by its season numbers 1, 2 and 3, where 1 - 'Vanakalam', 2 - 'Yasangi' and 3 - 'Summer'.",
            "dataSchema": "iudx:Number",
            "unitCode": "C62",
            "unitText": "Dimensionless"
          },
          "districtName": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "The name of the district at which the parcel land is located.",
            "dataSchema": "adex:Text"
          },
          "subdistrictName": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "The name of the mandal at which the parcel land is located.",
            "dataSchema": "adex:Text"
          },
          "clusterName": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "The name of the cluster at which the parcel land is located.",
            "dataSchema": "adex:Text"
          },
          "villageName": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "The name of the village at which the parcel land is located.",
            "dataSchema": "adex:Text"
          },
          "landIdentityInfo": {
            "type": [
              "LandIdentityDesc"
            ],
            "description": "The unique land identification information corresponding to this observation.",
            "baseSurveyNumber": {
              "type": [
                "ValueDescriptor"
              ],
              "description": "The base survey number assigned to the parcel land corresponding to this observation.",
              "dataSchema": "adex:Text"
            },
            "surveyNumber": {
              "type": [
                "ValueDescriptor"
              ],
              "description": "The unique code or number assigned to the parcel land for adminstrative purpose.",
              "dataSchema": "adex:Text"
            }
          },
          "landExtent": {
            "type": [
              "ValueDescriptor"
            ],
            "dataSchema": "iudx:Number",
            "unitCode": "ACR",
            "unitText": "acre",
            "description": "The extent of the parcel land in accordance with the cadastre."
          },
          "irrigationSource": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "The various types of irrigation for the agricultural land corresponding to this observation.",
            "dataSchema": "adex:Text"
          },
          "cropNameCommon": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "The name of the crop sown in the agricultural land corresponding to this observation.",
            "dataSchema": "adex:Text"
          },
          "cropVarietyName": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "The unique code for variety of the crop sown in the agricultural land corresponding to this observation.",
            "dataSchema": "adex:Text"
          },
          "cropArea": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "The extent of the parcel agricultural land which is measured in Guntas.",
            "dataSchema": "iudx:Number",
            "unitText": "guntas"
          },
          "observationDateTime": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "Last reported time of observation.",
            "dataSchema": "adex:DateTime"
          }
        },
        "dataSample": {
          "name": "జక్కుల ప్రమోద్",
          "phone": 9000203358,
          "year": 2022,
          "cropSeason": 1,
          "districtName": "KHAMMAM",
          "subdistrictName": "BONAKAL",
          "clusterName": "LAXMIPURAM",
          "villageName": "TUTIKUNTLA",
          "landIdentityInfo": {
            "baseSurveyNumber": "45",
            "surveyNumber": "45అ"
          },
          "landExtent": 0.375,
          "irrigationSource": "Tank",
          "cropNameCommon": " Paddy",
          "cropVarietyName": "BPT 5204",
          "cropArea": 0,
          "observationDateTime": "2021-08-11T13:41:14+5:30"
        },
        "location": {
          "geometry": {
            "coordinates": [
              [
                [
                  77.179011,
                  18.556975
                ],
                [
                  77.047585,
                  15.14819
                ],
                [
                  81.059914,
                  16.55208
                ],
                [
                  81.384916,
                  17.721272
                ],
                [
                  80.569225,
                  19.514793
                ],
                [
                  78.217742,
                  20.06644
                ],
                [
                  77.179011,
                  18.556975
                ]
              ]
            ],
            "type": "Polygon"
          },
          "type": "Place",
          "address": "Telangana"
        },
        "itemStatus": "ACTIVE",
        "ownerUserId": "fcc72273-858d-4dc3-9175-8727dd28d71e",
        "cos": "49f96c4c-e595-4fee-984c-43dededfba48",
        "itemCreatedAt": "2024-02-21T03:24:46+0530"
      },
      {
        "@context": "https://voc.iudx.org.in/",
        "type": [
          "iudx:Resource",
          "iudx:Irrigation",
          "adex:Resource",
          "adex:Irrigation"
        ],
        "id": "1d5d1a32-4afa-44fd-96e0-c99bd72119a8",
        "name": "pre-monsoon-water-quality-data",
        "label": "Pre Monsoon Water Quality Info in Telangana",
        "description": "Provides information about the Pre Monsoon Water Quality details such as electrical conductivity, calcium, chlorine, fluorine, nitrate, sulphate and sodium etc.",
        "tags": [
          "open data",
          "pre monsoon",
          "AgriCredit",
          "district",
          "crop",
          "subdistrict",
          "agriculture",
          "land"
        ],
        "accessPolicy": "OPEN",
        "apdURL": "acl-apd.adex.org.in",
        "provider": "fe6e514e-8260-4ab2-bc9f-a26c8a32a216",
        "resourceServer": "41bb4389-ebaf-4df7-a575-556ec6092a25",
        "resourceGroup": "eef88126-2011-4b9b-bcf8-41bae5f245e5",
        "resourceType": "DATASET",
        "adexResourceAPIs": [
          "ATTR"
        ],
        "iudxResourceAPIs": [
          "ATTR"
        ],
        "dataDescriptor": {
          "@context": "https://agrijson.adex.org.in/",
          "type": [
            "iudx:DataDescriptor",
            "iudx:Irrigation",
            "adex:DataDescriptor",
            "adex:Irrigation"
          ],
          "dataDescriptorLabel": "Data Descriptor Of Pre Monsoon Water Quality Data",
          "description": "Data attribute details provides information about the pre monsoon water quality details such as PH, E.C, TDS, CO3, HCO3, Cl, F, NO3, SO4, Na, K, Ca etc. in Telangana.",
          "districtName": {
            "description": "Name of the district corresponding to this observation.",
            "dataSchema": "adex:Text",
            "type": [
              "ValueDescriptor"
            ]
          },
          "subdistrictName": {
            "description": "Name of the subdistrict corresponding to this observation. A subdistrict is also called as mandal in the state of Telangana.",
            "dataSchema": "adex:Text",
            "type": [
              "ValueDescriptor"
            ]
          },
          "villageName": {
            "description": "Name of the village corresponding to this observation.",
            "dataSchema": "adex:Text",
            "type": [
              "ValueDescriptor"
            ]
          },
          "location": {
            "description": "Physical coordinates of cropland corresponding to this observation.",
            "dataSchema": "adex:Point",
            "type": [
              "ValueDescriptor"
            ]
          },
          "season": {
            "description": "Represents specific time of the year that has distinct weather patterns and conditions, such as summer, autumn (fall), etc.",
            "dataSchema": "adex:Text",
            "type": [
              "ValueDescriptor"
            ]
          },
          "pH": {
            "description": "The measure of the acidity or basicity.",
            "dataSchema": "adex:Number",
            "type": [
              "ValueDescriptor"
            ],
            "unitCode": "C62",
            "unitText": "dimensionless"
          },
          "electricalConductivity": {
            "description": "The measure of electrical conductivity of the entity corresponding to this observation.",
            "dataSchema": "adex:Number",
            "type": [
              "ValueDescriptor"
            ],
            "unitText": "decisiemens per meter [dS/m]"
          },
          "tds": {
            "description": "Observed value of Carbon trioxide in the entity under consideration.",
            "dataSchema": "adex:Number",
            "type": [
              "ValueDescriptor"
            ]
          },
          "co3": {
            "description": "Observed value of Carbon trioxide in the entity under consideration.",
            "dataSchema": "adex:Number",
            "type": [
              "ValueDescriptor"
            ]
          },
          "hco3": {
            "description": "Observed value of Bicarbonate in the entity under consideration.",
            "dataSchema": "adex:Number",
            "type": [
              "ValueDescriptor"
            ]
          },
          "cl": {
            "description": "Observed value of Chlorine in the entity under consideration.",
            "dataSchema": "adex:Number",
            "type": [
              "ValueDescriptor"
            ]
          },
          "fluorine": {
            "description": "Observed value of fluorine in the entity under consideration.",
            "dataSchema": "adex:Number",
            "type": [
              "ValueDescriptor"
            ]
          },
          "no3": {
            "description": "Observed value of Nitrate in the entity under consideration.",
            "dataSchema": "adex:Number",
            "type": [
              "ValueDescriptor"
            ]
          },
          "so4": {
            "description": "Observed value of Sulphate in the entity under consideration.",
            "dataSchema": "adex:Number",
            "type": [
              "ValueDescriptor"
            ]
          },
          "na": {
            "description": "Observed value of Sodium in the entity under consideration.",
            "dataSchema": "adex:Number",
            "type": [
              "ValueDescriptor"
            ]
          },
          "potassium": {
            "description": "Observed value of Potassium composition in the soil.",
            "dataSchema": "adex:Number",
            "type": [
              "ValueDescriptor"
            ],
            "unitText": "kilogram per hectare [kg/hectare]"
          },
          "ca": {
            "description": "Observed value of Calcium in the entity under consideration.",
            "dataSchema": "adex:Number",
            "type": [
              "ValueDescriptor"
            ]
          },
          "mg": {
            "description": "Observed value of Magnesium in the entity under consideration.",
            "dataSchema": "adex:Number",
            "type": [
              "ValueDescriptor"
            ]
          },
          "th": {
            "description": "Total Hardness (TH) is the measurement of the mineral content in the water sample.",
            "dataSchema": "adex:Number",
            "type": [
              "ValueDescriptor"
            ]
          },
          "sar": {
            "description": "Sodium Adsorption Ratio (SAR) is the measure of water suitability for irrigation usage. The value represents the relative amount of Sodium ions to the combined amount of calcium and magnesium ions in water.",
            "dataSchema": "adex:Number",
            "type": [
              "ValueDescriptor"
            ]
          },
          "category": {
            "description": "Represents the name of classification of an entity or service based on a particular aspect.",
            "dataSchema": "adex:Text",
            "type": [
              "ValueDescriptor"
            ]
          },
          "rsc": {
            "description": "Residual Sodium Carbonate (RSC) Index is the measure of alkalinity hazard of irrigation water for soil.",
            "dataSchema": "adex:Number",
            "type": [
              "ValueDescriptor"
            ]
          },
          "year": {
            "description": "Year corresponding to this observation and is described in YYYY format.",
            "dataSchema": "adex:Number",
            "type": [
              "ValueDescriptor"
            ]
          }
        },
        "dataSample": {
          "districtName": "ADILABAD",
          "subdistrictName": "Adilabad",
          "villageName": "Adilabad",
          "location": {
            "type": "Point",
            "coordinates": [
              91.280569,
              23.830214
            ]
          },
          "season": "premonsoon 2018",
          "pH": 8.21,
          "electricalConductivity": 140,
          "tds": 900.48,
          "co3": 0,
          "hco3": 240,
          "cl": 190,
          "fluorine": 0.34,
          "no3": 94.3377,
          "so4": 129,
          "na": 95,
          "potassium": 5,
          "ca": 48,
          "mg": 111.826,
          "th": 579.8108,
          "sar": 1.71534,
          "category": "C3S1-P.S.",
          "rsc": -6.796,
          "year": 2022
        },
        "location": {
          "type": "Place",
          "address": "Telangana",
          "geometry": {
            "coordinates": [
              [
                [
                  77.120821,
                  19.704752
                ],
                [
                  81.273653,
                  19.839154
                ],
                [
                  81.343529,
                  15.976888
                ],
                [
                  77.160163,
                  15.818332
                ],
                [
                  77.120821,
                  19.704752
                ]
              ]
            ],
            "type": "Polygon"
          }
        },
        "itemStatus": "ACTIVE",
        "ownerUserId": "6bdfa780-d8c0-4b2a-9a89-a1586d1d752f",
        "cos": "49f96c4c-e595-4fee-984c-43dededfba48",
        "itemCreatedAt": "2024-04-01T01:05:32+0530"
      },
      {
        "@context": "https://voc.iudx.org.in/",
        "type": [
          "iudx:Resource",
          "iudx:Irrigation",
          "adex:Resource",
          "adex:Irrigation"
        ],
        "id": "afe78be3-41d2-4869-acca-beeac57a213b",
        "name": "post-monsoon-water-quality-data",
        "label": "Post Monsoon Water Quality Info in Telangana",
        "description": "Provides information about the post monsoon water quality details such as electrical conductivity, calcium, chlorine, fluorine, nitrate, sulphate and sodium etc.",
        "tags": [
          "open data",
          "post monsoon",
          "district",
          "crop",
          "subdistrict",
          "agriculture",
          "land"
        ],
        "accessPolicy": "OPEN",
        "apdURL": "acl-apd.adex.org.in",
        "provider": "fe6e514e-8260-4ab2-bc9f-a26c8a32a216",
        "resourceServer": "41bb4389-ebaf-4df7-a575-556ec6092a25",
        "resourceGroup": "eef88126-2011-4b9b-bcf8-41bae5f245e5",
        "resourceType": "DATASET",
        "adexResourceAPIs": [
          "ATTR"
        ],
        "iudxResourceAPIs": [
          "ATTR"
        ],
        "dataArrivalInterval": "NonTemporal",
        "dataDescriptor": {
          "@context": "https://agrijson.adex.org.in/",
          "type": [
            "iudx:DataDescriptor",
            "iudx:Irrigation",
            "adex:DataDescriptor",
            "adex:Irrigation"
          ],
          "dataDescriptorLabel": "Data Descriptor Of Post Monsoon Water Quality Data",
          "description": "Data attribute details provides information about the post monsoon water quality details such as PH, E.C, TDS, CO3, HCO3, Cl, F, NO3, SO4, Na, K, Ca etc.",
          "districtName": {
            "description": "Name of the district corresponding to this observation.",
            "dataSchema": "adex:Text",
            "type": [
              "ValueDescriptor"
            ]
          },
          "subdistrictName": {
            "description": "Name of the subdistrict corresponding to this observation. A subdistrict is also called as mandal in Telangana",
            "dataSchema": "adex:Text",
            "type": [
              "ValueDescriptor"
            ]
          },
          "villageName": {
            "description": "Name of the village corresponding to this observation.",
            "dataSchema": "adex:Text",
            "type": [
              "ValueDescriptor"
            ]
          },
          "location": {
            "description": "Physical coordinates of cropland corresponding to this observation.",
            "dataSchema": "adex:Point",
            "type": [
              "ValueDescriptor"
            ]
          },
          "season": {
            "description": "Represents specific time of the year that has distinct weather patterns and conditions, such as summer, autumn (fall), etc.",
            "dataSchema": "adex:Text",
            "type": [
              "ValueDescriptor"
            ]
          },
          "pH": {
            "description": "The measure of the acidity or basicity.",
            "dataSchema": "adex:Number",
            "type": [
              "ValueDescriptor"
            ],
            "unitCode": "C62",
            "unitText": "dimensionless"
          },
          "electricalConductivity": {
            "description": "The measure of electrical conductivity of the entity corresponding to this observation.",
            "dataSchema": "adex:Number",
            "type": [
              "ValueDescriptor"
            ],
            "unitText": "decisiemens per meter [dS/m]"
          },
          "tds": {
            "description": "Observed value of Carbon trioxide in the entity under consideration.",
            "dataSchema": "adex:Number",
            "type": [
              "ValueDescriptor"
            ]
          },
          "co3": {
            "description": "Observed value of Carbon trioxide in the entity under consideration.",
            "dataSchema": "adex:Number",
            "type": [
              "ValueDescriptor"
            ]
          },
          "hco3": {
            "description": "Observed value of Bicarbonate in the entity under consideration.",
            "dataSchema": "adex:Number",
            "type": [
              "ValueDescriptor"
            ]
          },
          "cl": {
            "description": "Observed value of Chlorine in the entity under consideration.",
            "dataSchema": "adex:Number",
            "type": [
              "ValueDescriptor"
            ]
          },
          "fluorine": {
            "description": "Observed value of fluorine in the entity under consideration.",
            "dataSchema": "adex:Number",
            "type": [
              "ValueDescriptor"
            ]
          },
          "no3": {
            "description": "Observed value of Nitrate in the entity under consideration.",
            "dataSchema": "adex:Number",
            "type": [
              "ValueDescriptor"
            ]
          },
          "so4": {
            "description": "Observed value of Sulphate in the entity under consideration.",
            "dataSchema": "adex:Number",
            "type": [
              "ValueDescriptor"
            ]
          },
          "na": {
            "description": "Observed value of Sodium in the entity under consideration.",
            "dataSchema": "adex:Number",
            "type": [
              "ValueDescriptor"
            ]
          },
          "potassium": {
            "description": "Observed value of Potassium composition in the soil.",
            "dataSchema": "adex:Number",
            "type": [
              "ValueDescriptor"
            ],
            "unitText": "kilogram per hectare [kg/hectare]"
          },
          "ca": {
            "description": "Observed value of Calcium in the entity under consideration.",
            "dataSchema": "adex:Number",
            "type": [
              "ValueDescriptor"
            ]
          },
          "mg": {
            "description": "Observed value of Magnesium in the entity under consideration.",
            "dataSchema": "adex:Number",
            "type": [
              "ValueDescriptor"
            ]
          },
          "th": {
            "description": "Total Hardness (TH) is the measurement of the mineral content in the water sample.",
            "dataSchema": "adex:Number",
            "type": [
              "ValueDescriptor"
            ]
          },
          "sar": {
            "description": "Sodium Adsorption Ratio (SAR) is the measure of water suitability for irrigation usage. The value represents the relative amount of Sodium ions to the combined amount of calcium and magnesium ions in water.",
            "dataSchema": "adex:Number",
            "type": [
              "ValueDescriptor"
            ]
          },
          "category": {
            "description": "Represents the name of classification of an entity or service based on a particular aspect.",
            "dataSchema": "adex:Text",
            "type": [
              "ValueDescriptor"
            ]
          },
          "rsc": {
            "description": "Residual Sodium Carbonate (RSC) Index is the measure of alkalinity hazard of irrigation water for soil.",
            "dataSchema": "adex:Number",
            "type": [
              "ValueDescriptor"
            ]
          },
          "year": {
            "description": "Year corresponding to this observation and is described in YYYY format.",
            "dataSchema": "adex:Number",
            "type": [
              "ValueDescriptor"
            ]
          }
        },
        "dataSample": {
          "districtName": "ADILABAD",
          "subdistrictName": "Adilabad",
          "villageName": "Adilabad",
          "location": {
            "type": "Point",
            "coordinates": [
              91.280569,
              23.830214
            ]
          },
          "season": "premonsoon 2018",
          "pH": 8.21,
          "electricalConductivity": 140,
          "tds": 900.48,
          "co3": 0,
          "hco3": 240,
          "cl": 190,
          "fluorine": 0.34,
          "no3": 94.3377,
          "so4": 129,
          "na": 95,
          "potassium": 5,
          "ca": 48,
          "mg": 111.826,
          "th": 579.8108,
          "sar": 1.71534,
          "category": "C3S1-P.S.",
          "rsc": -6.796,
          "year": 2022
        },
        "location": {
          "type": "Place",
          "address": "Telangana",
          "geometry": {
            "coordinates": [
              [
                [
                  77.120821,
                  19.704752
                ],
                [
                  81.273653,
                  19.839154
                ],
                [
                  81.343529,
                  15.976888
                ],
                [
                  77.160163,
                  15.818332
                ],
                [
                  77.120821,
                  19.704752
                ]
              ]
            ],
            "type": "Polygon"
          }
        },
        "itemStatus": "ACTIVE",
        "ownerUserId": "6bdfa780-d8c0-4b2a-9a89-a1586d1d752f",
        "cos": "49f96c4c-e595-4fee-984c-43dededfba48",
        "itemCreatedAt": "2024-04-01T01:05:28+0530"
      },
      {
        "@context": "https://voc.iudx.org.in/",
        "id": "bf3f8f28-5949-436f-acce-893c87494462",
        "type": [
          "adex:Resource",
          "adex:AgriMarket",
          "iudx:Resource",
          "iudx:AgriMarket"
        ],
        "name": "chilli-quality-info",
        "label": "Chilli Sampling for Quality in Telangana State",
        "description": "Publishes the information of chilli sampling performed by Digital Green at various Rythu vedhikasa as an initiative by Saagu Baagu Project of Telangana. The chilli sampling information for the previous month  is published  on 10th of every month.",
        "tags": [
          "chilli",
          "crop",
          "grade",
          "market",
          "price",
          "variety",
          "mandi",
          "district",
          "agency",
          "traders",
          "procurement",
          "prices",
          "agricultural produce",
          "spices"
        ],
        "accessPolicy": "SECURE",
        "apdURL": "acl-apd.adex.org.in",
        "provider": "55862fb4-fed8-4600-bd06-749ff1467037",
        "resourceServer": "41bb4389-ebaf-4df7-a575-556ec6092a25",
        "resourceGroup": "90e216bc-8129-44be-a4ad-f4e8c1981b71",
        "resourceType": "MESSAGESTREAM",
        "adexResourceAPIs": [
          "TEMPORAL",
          "ATTR"
        ],
        "iudxResourceAPIs": [
          "TEMPORAL",
          "ATTR"
        ],
        "dataDescriptor": {
          "@context": "https://agrijson.org/",
          "type": [
            "adex:DataDescriptor",
            "adex:AgriMarket",
            "iudx:Resource",
            "iudx:AgriMarket"
          ],
          "dataDescriptorLabel": "Data descriptor for the Chilli Sampling Information in the Telangana State.",
          "description": "Data attribute details of the chilli sampling information in the Telangana state.",
          "sampleID": {
            "description": "The unique ID representing the chilli sample corresponding to this observation",
            "dataSchema": "adex:Text",
            "type": [
              "ValueDescriptor"
            ]
          },
          "warehouseName": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "Name of the ware house corresponding to this observation..",
            "dataSchema": "iudx:Text"
          },
          "stateName": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "Name of the state corresponding to this observation.",
            "dataSchema": "iudx:Text"
          },
          "arrivalQuantity": {
            "type": [
              "ValueDescriptor"
            ],
            "dataSchema": "adex:Number",
            "unitCode": "KGM",
            "unitText": "kilogram",
            "description": "The quantity of the green chilli corresponding to this observation."
          },
          "productGrade": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "The grade of the green chilli corresponding to this observation.",
            "dataSchema": "iudx:Text"
          },
          "subdistrictName": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "Name of the subdistrict corresponding to this observation. A subdistrict is also called as a tehsil, mandal, tahsil, tahasil, taluka, taluk, or taluq across the Indian states.",
            "dataSchema": "iudx:Text"
          },
          "locality": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "Name of the locality corresponding to this observation.",
            "dataSchema": "adex:Text"
          },
          "districtName": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "The name of the district corresponding to this observation.",
            "dataSchema": "adex:Text"
          },
          "villageName": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "Name of the village corresponding to this observation.",
            "dataSchema": "adex:Text"
          },
          "brokenProduce": {
            "description": "Percentage of chillies that are physically broken or cracked, impacting overall integrity.",
            "type": [
              "ValueDescriptor"
            ],
            "unitCode": "P1",
            "unitText": "percent",
            "dataSchema": "iudx:Number"
          },
          "ddp": {
            "description": "Percentage of Damaged & Discolored Pods (DDP), such as chilli pods with visible damage, discoloration, or other aesthetic defects.",
            "type": [
              "ValueDescriptor"
            ],
            "unitCode": "P1",
            "unitText": "percent",
            "dataSchema": "iudx:Number"
          },
          "foreignMatter": {
            "description": "Percentage of any unwanted materials, such as dirt, stones, or contaminants. in the green chilli",
            "type": [
              "ValueDescriptor"
            ],
            "unitCode": "P1",
            "unitText": "percent",
            "dataSchema": "iudx:Number"
          },
          "fineProduce": {
            "description": "Percentage of chillies that meet the desired quality standards without significant defects.",
            "type": [
              "ValueDescriptor"
            ],
            "unitCode": "P1",
            "unitText": "percent",
            "dataSchema": "iudx:Number"
          },
          "mip": {
            "description": "Percentage of Mold Infested Pods (MIP), such as chilli pods showing signs of mold growth, indicating spoilage or improper storage.",
            "type": [
              "ValueDescriptor"
            ],
            "unitCode": "P1",
            "unitText": "percent",
            "dataSchema": "iudx:Number"
          },
          "pows": {
            "description": "Percentage of Pods without Stem (POWS), such as chillies lacking the stem, which may impact overall appearance and handling.",
            "type": [
              "ValueDescriptor"
            ],
            "unitCode": "P1",
            "unitText": "percent",
            "dataSchema": "iudx:Number"
          },
          "moistureLevel": {
            "description": "Percentage of moisture content in the green chilli corresponding to this observation.",
            "type": [
              "ValueDescriptor"
            ],
            "unitCode": "P1",
            "unitText": "percent",
            "dataSchema": "iudx:Number"
          },
          "observationDateTime": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "The date of inspection of the chillies corresponding to this observation.",
            "dataSchema": "adex:DateTime"
          }
        },
        "dataSample": {
          "sampleID": "c1f3843f-b4b1-434a-8dae-2e82dd07a5c3",
          "villageName": "Kharar",
          "districtName": "Sonepat",
          "subdistrictName": "Mohali",
          "locality": "MPK 05",
          "warehouseName": "MPK 05",
          "productGrade": "A (Best)",
          "arrivalQuantity": 2000.0,
          "brokenProduce": 52.75,
          "ddp": 0.0,
          "foreignMatter": 9.22,
          "fineProduce": 0.0,
          "mip": 0.21,
          "pows": 37.83,
          "moistureLevel": 12.9,
          "observationDateTime": "2023-02-02T00:00:00+05:30"
        },
        "location": {
          "geometry": {
            "coordinates": [
              [
                [
                  77.179011,
                  18.556975
                ],
                [
                  77.047585,
                  15.14819
                ],
                [
                  81.059914,
                  16.55208
                ],
                [
                  81.384916,
                  17.721272
                ],
                [
                  80.569225,
                  19.514793
                ],
                [
                  78.217742,
                  20.06644
                ],
                [
                  77.179011,
                  18.556975
                ]
              ]
            ],
            "type": "Polygon"
          },
          "type": "Place",
          "address": "Telangana"
        },
        "itemStatus": "ACTIVE",
        "ownerUserId": "5bddd541-7a10-4960-b048-007477cf9c5d",
        "cos": "49f96c4c-e595-4fee-984c-43dededfba48",
        "itemCreatedAt": "2024-03-15T06:31:02+0530"
      },
      {
        "@context": "https://voc.iudx.org.in/",
        "type": [
          "iudx:Resource",
          "iudx:AgriCredit",
          "adex:Resource",
          "adex:AgriCredit"
        ],
        "id": "2ec4827d-2ca8-4256-b166-3351ae38e63a",
        "name": "agri-credit-disbursment-info",
        "label": "Year Wise Agricultural Credit Disbursment Info in Telangana",
        "description": "Provides information about the Crop Loan Targets & Achievements, Agri Term Loans Targets & Achievements, and Agri Allied Activities Targets & Achievements along with their percentages and totals from the year 2011-2012 to 2016-2017.",
        "tags": [
          "open data",
          "AgriCredit",
          "district",
          "crop",
          "subdistrict",
          "agriculture",
          "land"
        ],
        "accessPolicy": "OPEN",
        "apdURL": "acl-apd.adex.org.in",
        "provider": "fe6e514e-8260-4ab2-bc9f-a26c8a32a216",
        "resourceServer": "41bb4389-ebaf-4df7-a575-556ec6092a25",
        "resourceGroup": "7deef963-f739-4d7e-8443-4f115166c1fa",
        "resourceType": "DATASET",
        "adexResourceAPIs": [
          "ATTR"
        ],
        "iudxResourceAPIs": [
          "ATTR"
        ],
        "dataArrivalInterval": "NonTemporal",
        "dataDescriptor": {
          "@context": "https://agrijson.adex.org.in/",
          "type": [
            "iudx:DataDescriptor",
            "iudx:AgriCredit",
            "adex:DataDescriptor",
            "adex:AgriCredit"
          ],
          "dataDescriptorLabel": "Data descriptor agricultural credit disbursment info in Telangana state",
          "description": "Data attribute details of information about the Crop Loan Targets & Achievements, Agri Term Loans Targets & Achievements, and Agri Allied Activities Targets & Achievements along with their percentages and totals from the year 2011-2012 to 2016-2017.",
          "year": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "The beginning year of the survey or assessment corresponds to this observation and is described in the YYYY format.",
            "dataSchema": "adex:Number",
            "unitCode": "C62",
            "unitText": "dimensionless"
          },
          "evaluationYear": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "The period during which a survey or assessment has been carried out.",
            "dataSchema": "adex:Text"
          },
          "loanType": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "The specific type of financial assistance provided to individuals or entities. For eg., crop loan, term loan etc.",
            "dataSchema": "adex:Text"
          },
          "loanTargetAmount": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "The total amount of money planned to be disbursed as agricultural credit for a particular loan type, by the government or financial institution within a certain time period.",
            "dataSchema": "adex:Number",
            "unitCode": "INR",
            "unitText": "Indian Rupee"
          },
          "loanAchievementAmount": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "The total amount of money actually disbursed as agricultural credit for a particular loan type, by the government or financial institution within a certain time period.",
            "dataSchema": "adex:Number",
            "unitCode": "INR",
            "unitText": "Indian Rupee"
          },
          "achievementRate": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "The ratio of the actual loan amount disbursed to the loan amount targeted to be disbursed for a particular loan type, expressed as a percentage, denoting the level of attainment of the credit goals.",
            "dataSchema": "adex:Number",
            "unitCode": "P1",
            "unitText": "percent"
          },
          "totalTargetAmount": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "The total amount of money targeted to be disbursed across all loan types within a specific period.",
            "dataSchema": "adex:Number",
            "unitCode": "INR",
            "unitText": "Indian Rupee"
          },
          "totalAchievementAmount": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "The total amount of money actually disbursed across all loan types within a specific period.",
            "dataSchema": "adex:Number",
            "unitCode": "INR",
            "unitText": "Indian Rupee"
          },
          "totalAchievementRate": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "The ratio of the actual loan amount disbursed in total to the total loan amount targeted to be disbursed across all loan types, expressed as a percentage, denoting the level of attainment of the credit goals.",
            "dataSchema": "adex:Number",
            "unitCode": "P1",
            "unitText": "percent"
          }
        },
        "dataSample": {
          "year": 2011,
          "evaluationYear": "2011-12",
          "loanType": "crop loan",
          "loanTargetAmount": 3298.0,
          "loanAchievementAmount": 11787.0,
          "achievementRate": 115.19,
          "totalTargetAmount": 16123.0,
          "totalAchievementAmount": 22899.0,
          "totalAchievementRate": 142.03
        },
        "location": {
          "type": "Place",
          "address": "Telangana",
          "geometry": {
            "coordinates": [
              [
                [
                  77.120821,
                  19.704752
                ],
                [
                  81.273653,
                  19.839154
                ],
                [
                  81.343529,
                  15.976888
                ],
                [
                  77.160163,
                  15.818332
                ],
                [
                  77.120821,
                  19.704752
                ]
              ]
            ],
            "type": "Polygon"
          }
        },
        "itemStatus": "ACTIVE",
        "ownerUserId": "6bdfa780-d8c0-4b2a-9a89-a1586d1d752f",
        "cos": "49f96c4c-e595-4fee-984c-43dededfba48",
        "itemCreatedAt": "2024-04-01T01:05:19+0530"
      },
      {
        "@context": "https://voc.iudx.org.in/",
        "id": "3ac4dc21-10be-4424-805b-5b40a571d5ed",
        "type": [
          "iudx:Resource",
          "iudx:Weather",
          "adex:Resource",
          "adex:Weather"
        ],
        "name": "telangana-subdistrict-weather-info",
        "label": "Subdistrict Level Weather Information from Telangana",
        "description": "Publishes information on daily weather conditions, including temperature, wind speed, and precipitation, observed from every weather station in Telangana on monthly basis.",
        "tags": [
          "open data",
          "environment",
          "weather",
          "weather monitoring sensors",
          "rainfall",
          "precipitation",
          "weather information",
          "humidity",
          "weather forecast",
          "meteorological department",
          "temperature"
        ],
        "accessPolicy": "OPEN",
        "apdURL": "acl-apd.adex.org.in",
        "provider": "fe6e514e-8260-4ab2-bc9f-a26c8a32a216",
        "resourceServer": "41bb4389-ebaf-4df7-a575-556ec6092a25",
        "resourceGroup": "5a1ebef8-ddb2-4ee7-af4c-9edc0d4297d1",
        "resourceType": "MESSAGESTREAM",
        "adexResourceAPIs": [
          "TEMPORAL",
          "ATTR"
        ],
        "iudxResourceAPIs": [
          "TEMPORAL",
          "ATTR"
        ],
        "dataArrivalInterval": "Every start of the month",
        "dataDescriptor": {
          "@context": "https://agrijson.org/",
          "type": [
            "iudx:DataDescriptor",
            "iudx:Weather",
            "adex:DataDescriptor",
            "adex:Weather"
          ],
          "dataDescriptorLabel": "Data descriptor for weather information in Telangana state",
          "description": "Data attribute details of weather monitoring system in Telangana state.",
          "districtName": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "Name of the district corresponding to this observation.",
            "dataSchema": "adex:Text"
          },
          "subdistrictName": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "Name of the subdistrict or mandal corresponding to this observation.",
            "dataSchema": "adex:Text"
          },
          "precipitation": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "Cumulative values of precipitation/rainfall for the date corresponding to this observation.",
            "unitCode": "MMT",
            "unitText": "millimetre (mm)",
            "dataSchema": "adex:Number"
          },
          "airTemperature": {
            "type": [
              "TimeSeriesAggregation"
            ],
            "description": "The aggregated value for air temperature in degree Celsius over 24 hours of the date corresponding to this observation.",
            "maxOverTime": {
              "type": [
                "ValueDescriptor"
              ],
              "description": "Maximum value of air temperature over 24 hours of the date corresponding to this observation.",
              "dataSchema": "adex:Number",
              "unitCode": "CEL",
              "unitText": "degree Celsius (C)"
            },
            "minOverTime": {
              "type": [
                "ValueDescriptor"
              ],
              "description": "Minimum value of air temperature over 24 hours of the date corresponding to this observation.",
              "dataSchema": "adex:Number",
              "unitCode": "CEL",
              "unitText": "degree Celsius (C)"
            }
          },
          "relativeHumidity": {
            "type": [
              "TimeSeriesAggregation"
            ],
            "description": "The aggregated values for humidity (water vapour in air) over 24 hours of the date corresponding to this observation.",
            "maxOverTime": {
              "type": [
                "ValueDescriptor"
              ],
              "description": "Maximum value of relative humidity over 24 hours of the date corresponding to this observation.",
              "dataSchema": "adex:Number",
              "unitCode": "P1",
              "unitText": "percent"
            },
            "minOverTime": {
              "type": [
                "ValueDescriptor"
              ],
              "description": "Minimum value of of relative humidity over 24 hours of the date corresponding to this observation.",
              "dataSchema": "adex:Number",
              "unitCode": "P1",
              "unitText": "percent"
            }
          },
          "windSpeed": {
            "type": [
              "TimeSeriesAggregation"
            ],
            "description": "The aggregated values for wind speed over 24 hours of the date corresponding to this observation.",
            "maxOverTime": {
              "type": [
                "ValueDescriptor"
              ],
              "description": "Maximum value of wind speed over 24 hours of the date corresponding to this observation.",
              "dataSchema": "adex:Number",
              "unitCode": "P1",
              "unitText": "percent"
            },
            "minOverTime": {
              "type": [
                "ValueDescriptor"
              ],
              "description": "Minimum value of wind speed over 24 hours of the date corresponding to this observation.",
              "dataSchema": "adex:Number",
              "unitCode": "P1",
              "unitText": "percent"
            }
          },
          "observationDateTime": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "The date which the weather information corresponds to.",
            "dataSchema": "adex:DateTime"
          }
        },
        "dataSample": {
          "districtName": "Adilabad",
          "subdistrictName": "Tamsi",
          "precipitation": 0.0,
          "airTemperature": {
            "maxOverTime": 30.5,
            "minOverTime": 15.9
          },
          "relativeHumidity": {
            "maxOverTime": 98.0,
            "minOverTime": 62.3
          },
          "windSpeed": {
            "maxOverTime": 5.3,
            "minOverTime": 0.0
          },
          "observationDateTime": "2023-02-01T00:00:00+05:30"
        },
        "location": {
          "type": "Place",
          "address": "Telangana",
          "geometry": {
            "coordinates": [
              [
                [
                  77.120821,
                  19.704752
                ],
                [
                  81.273653,
                  19.839154
                ],
                [
                  81.343529,
                  15.976888
                ],
                [
                  77.160163,
                  15.818332
                ],
                [
                  77.120821,
                  19.704752
                ]
              ]
            ],
            "type": "Polygon"
          }
        },
        "itemStatus": "ACTIVE",
        "ownerUserId": "6bdfa780-d8c0-4b2a-9a89-a1586d1d752f",
        "cos": "49f96c4c-e595-4fee-984c-43dededfba48",
        "itemCreatedAt": "2024-04-01T01:05:44+0530"
      },
      {
        "@context": "https://voc.iudx.org.in/",
        "type": [
          "iudx:Resource",
          "iudx:Irrigation",
          "adex:Resource",
          "adex:Irrigation"
        ],
        "id": "0e5294b8-8eb8-4ee5-9309-95fe5a426e76",
        "name": "tg-reservoir-water-storage",
        "label": "Reservoir Water Storage Level Details in Telangana",
        "description": "Publishes information about the water storage level details of reservoir in Telangana. The dataset is dynamic with update frequency of once per month",
        "tags": [
          "open data",
          "AgriCredit",
          "district",
          "crop",
          "subdistrict",
          "agriculture",
          "land"
        ],
        "accessPolicy": "OPEN",
        "apdURL": "acl-apd.adex.org.in",
        "provider": "fe6e514e-8260-4ab2-bc9f-a26c8a32a216",
        "resourceServer": "41bb4389-ebaf-4df7-a575-556ec6092a25",
        "resourceGroup": "d142b39d-0df3-46ee-b51e-b528f9bea214",
        "resourceType": "MESSAGESTREAM",
        "adexResourceAPIs": [
          "TEMPORAL",
          "ATTR"
        ],
        "iudxResourceAPIs": [
          "TEMPORAL",
          "ATTR"
        ],
        "dataArrivalInterval": "Every start of the month",
        "dataDescriptor": {
          "@context": "https://agrijson.adex.org.in/",
          "type": [
            "iudx:DataDescriptor",
            "iudx:Irrigation",
            "adex:DataDescriptor",
            "adex:Irrigation"
          ],
          "dataDescriptorLabel": "Data Descriptor about the Reservoir Water Storage Level Details in Telangana",
          "description": "Data attribute details provides information about the Reservoir water storage level details in Telangana.",
          "reservoirID": {
            "description": "The unique ID referring to the water reservoir corresponding to this observation.",
            "dataSchema": "adex:Text",
            "type": [
              "ValueDescriptor"
            ]
          },
          "reservoirName": {
            "description": "The name of the water reservoir corresponding to this observation.",
            "dataSchema": "adex:Text",
            "type": [
              "ValueDescriptor"
            ]
          },
          "riverBasin": {
            "description": "The name of the river/stream corresponding to this observation.",
            "dataSchema": "adex:Text",
            "type": [
              "ValueDescriptor"
            ]
          },
          "fullReservoirLevel": {
            "description": "The maximum level the water in the reservoir is designed to reach.",
            "dataSchema": "adex:Number",
            "type": [
              "ValueDescriptor"
            ]
          },
          "totalCapacity": {
            "description": "Represents the total volume of water that the reservoir corresponding to this observation can hold.",
            "dataSchema": "adex:Number",
            "type": [
              "ValueDescriptor"
            ]
          },
          "waterLevel": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "Current water level in reservoir corresponding to this observation.",
            "unitText": "Feet",
            "unitCode": "ft",
            "dataSchema": "iudx:Number"
          },
          "currentCapacity": {
            "description": "The current volume of water stored in the reservoir corresponding to this observation.",
            "dataSchema": "adex:Number",
            "type": [
              "ValueDescriptor"
            ]
          },
          "inflow": {
            "description": "Indicates the rate at which water enters into the reservoir corresponding to this observation.",
            "dataSchema": "adex:Number",
            "type": [
              "ValueDescriptor"
            ],
            "unitCode": "K6",
            "unitText": "kilolitre"
          },
          "outflow": {
            "description": "Indicates the rate at which water flows out of the reservoir corresponding to this observation.",
            "dataSchema": "adex:Number",
            "type": [
              "ValueDescriptor"
            ],
            "unitCode": "K6",
            "unitText": "kilolitre"
          },
          "date": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "Last recorded date at when the readings are reported corresponding to this observation and is described in YYYY-MM-DD format, for eg. '2020-11-05'.",
            "dataSchema": "iudx:Text"
          },
          "observationDateTime": {
            "description": "Last reported time of observation.",
            "dataSchema": "adex:DateTime",
            "type": [
              "ValueDescriptor"
            ]
          }
        },
        "dataSample": {
          "reservoirID": "BOGGULAVAGU",
          "reservoirName": "BOGGULAVAGU",
          "riverBasin": "Godavari Basin",
          "date": "2023-07-14",
          "fullReservoirLevel": 523.0,
          "totalCapacity": 0.40700001,
          "waterLevel": 0.0,
          "currentCapacity": 0.0,
          "inflow": 0.0,
          "outflow": 0.0,
          "observationDateTime": "2023-07-14T00:00:00+05:30"
        },
        "location": {
          "type": "Place",
          "address": "Telangana",
          "geometry": {
            "coordinates": [
              [
                [
                  77.120821,
                  19.704752
                ],
                [
                  81.273653,
                  19.839154
                ],
                [
                  81.343529,
                  15.976888
                ],
                [
                  77.160163,
                  15.818332
                ],
                [
                  77.120821,
                  19.704752
                ]
              ]
            ],
            "type": "Polygon"
          }
        },
        "itemStatus": "ACTIVE",
        "ownerUserId": "6bdfa780-d8c0-4b2a-9a89-a1586d1d752f",
        "cos": "49f96c4c-e595-4fee-984c-43dededfba48",
        "itemCreatedAt": "2024-04-01T01:05:40+0530"
      },
      {
        "@context": "https://voc.iudx.org.in/",
        "type": [
          "iudx:Resource",
          "iudx:LandParcel",
          "adex:Resource",
          "adex:LandParcel"
        ],
        "id": "21c72c11-13fd-44f5-b285-daf8e1d8eae8",
        "name": "agri-land-holding-info",
        "label": "District Level Agricultural Land Holdings Info in Telangana",
        "description": "Provides information on the count of marginal, small, semimedium, medium and Large land holdings in each district of the Telangana state as per agriculture census.",
        "tags": [
          "open data",
          "LandParcel",
          "district",
          "crop",
          "subdistrict",
          "agriculture",
          "land"
        ],
        "accessPolicy": "OPEN",
        "apdURL": "acl-apd.adex.org.in",
        "provider": "fe6e514e-8260-4ab2-bc9f-a26c8a32a216",
        "resourceServer": "41bb4389-ebaf-4df7-a575-556ec6092a25",
        "resourceGroup": "85f65527-8743-41fd-a1cd-785db5f77231",
        "resourceType": "DATASET",
        "adexResourceAPIs": [
          "ATTR"
        ],
        "iudxResourceAPIs": [
          "ATTR"
        ],
        "dataArrivalInterval": "NonTemporal",
        "dataDescriptor": {
          "@context": "https://agrijson.adex.org.in/",
          "type": [
            "iudx:DataDescriptor",
            "iudx:LandParcel",
            "adex:DataDescriptor",
            "adex:LandParcel"
          ],
          "dataDescriptorLabel": "Data descriptor for land holdings information in Telangana state",
          "description": "Data attribute details of information on the number of land holdings in Telangana state. The size of the land holding is defined as per agricultural sensus where Marginal - Less than 1 Hectare,  Small - Between 1 & 2 Hectares,  Small-Medium -Between 2 & 4 Hectares, Medium - Between 4 & 10 Hectares, Large - More than 10 Hectares",
          "districtName": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "Name of the district corresponding to this observation.",
            "dataSchema": "adex:Text"
          },
          "totalCount": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "Total number of land parcels as per the agricultural census.",
            "dataSchema": "adex:Number"
          },
          "landExtentType": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "Type of the land corresponding to this observation. The type of land is defined as per agricultural sensus where Marginal - Less than 1 Hectare,  Small - Between 1 & 2 Hectares,  Small-Medium -Between 2 & 4 Hectares, Medium - Between 4 & 10 Hectares, Large - More than 10 Hectares",
            "dataSchema": "adex:Text"
          }
        },
        "dataSample": {
          "districtName": "YADADRI",
          "totalCount": 19565,
          "landExtentType": "semimedium"
        },
        "location": {
          "type": "Place",
          "address": "Telangana",
          "geometry": {
            "coordinates": [
              [
                [
                  77.120821,
                  19.704752
                ],
                [
                  81.273653,
                  19.839154
                ],
                [
                  81.343529,
                  15.976888
                ],
                [
                  77.160163,
                  15.818332
                ],
                [
                  77.120821,
                  19.704752
                ]
              ]
            ],
            "type": "Polygon"
          }
        },
        "itemStatus": "ACTIVE",
        "ownerUserId": "6bdfa780-d8c0-4b2a-9a89-a1586d1d752f",
        "cos": "49f96c4c-e595-4fee-984c-43dededfba48",
        "itemCreatedAt": "2024-04-01T01:05:23+0530"
      },
      {
        "@context": "https://voc.iudx.org.in/",
        "type": [
          "iudx:Resource",
          "iudx:Irrigation",
          "adex:Resource",
          "adex:Irrigation"
        ],
        "id": "d578e0f9-49a5-47c2-bf22-2c132b715c43",
        "name": "tg-water-level-details",
        "label": "Village-level Ground Water Level Details in Telangana",
        "description": "Provides information about the ground water level of each village in the state of Telangana.",
        "tags": [
          "open data",
          "AgriCredit",
          "district",
          "crop",
          "subdistrict",
          "agriculture",
          "land"
        ],
        "accessPolicy": "OPEN",
        "apdURL": "acl-apd.adex.org.in",
        "provider": "fe6e514e-8260-4ab2-bc9f-a26c8a32a216",
        "resourceServer": "41bb4389-ebaf-4df7-a575-556ec6092a25",
        "resourceGroup": "b401e476-9e5f-47ef-ac85-ec1ce50ff240",
        "resourceType": "DATASET",
        "adexResourceAPIs": [
          "ATTR"
        ],
        "iudxResourceAPIs": [
          "ATTR"
        ],
        "dataDescriptor": {
          "@context": "https://agrijson.adex.org.in/",
          "type": [
            "iudx:DataDescriptor",
            "iudx:Irrigation",
            "adex:DataDescriptor",
            "adex:Irrigation"
          ],
          "dataDescriptorLabel": "Data Descriptor Of Water Level Details in Telangana State",
          "description": "Data attribute details provides information about the ground water level for villages in Telangana.",
          "districtName": {
            "description": "Name of the district corresponding to this observation.",
            "dataSchema": "adex:Text",
            "type": [
              "ValueDescriptor"
            ]
          },
          "subdistrictName": {
            "description": "The name of the sub district corresponding to this observation.",
            "dataSchema": "adex:Text",
            "type": [
              "ValueDescriptor"
            ]
          },
          "villageName": {
            "description": "The name of the village corresponding to this observation.",
            "dataSchema": "adex:Text",
            "type": [
              "ValueDescriptor"
            ]
          },
          "location": {
            "type": "Point",
            "coordinates": [
              91.280569,
              23.830214
            ]
          },
          "date": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "Date corresponding to this observation and is described in YYYY-MM-DD format, for eg. '2020-11-05'.",
            "dataSchema": "iudx:Text"
          },
          "waterLevel": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "The ground water level corresponding to this observation",
            "dataSchema": "iudx:Number"
          }
        },
        "dataSample": {
          "districtName": "KUMURAM BHEEM",
          "subdistrictName": "Tiryani",
          "villageName": "Tiryani",
          "location": {
            "type": "Point",
            "coordinates": [
              91.280569,
              23.830214
            ]
          },
          "date": "2023-07-14",
          "waterLevel": 1
        },
        "location": {
          "type": "Place",
          "address": "Telangana",
          "geometry": {
            "coordinates": [
              [
                [
                  77.120821,
                  19.704752
                ],
                [
                  81.273653,
                  19.839154
                ],
                [
                  81.343529,
                  15.976888
                ],
                [
                  77.160163,
                  15.818332
                ],
                [
                  77.120821,
                  19.704752
                ]
              ]
            ],
            "type": "Polygon"
          }
        },
        "itemStatus": "ACTIVE",
        "ownerUserId": "6bdfa780-d8c0-4b2a-9a89-a1586d1d752f",
        "cos": "49f96c4c-e595-4fee-984c-43dededfba48",
        "itemCreatedAt": "2024-04-01T01:05:36+0530"
      },
      {
        "@context": "https://voc.iudx.org.in/",
        "type": [
          "iudx:Resource",
          "iudx:LandParcel",
          "adex:Resource",
          "adex:LandParcel"
        ],
        "id": "5f5465f3-5313-4f28-a24a-34a259a0622f",
        "name": "tg-year-wise-trend-of-food-corps",
        "label": "Year Wise Trend Of Food Crops in Telangana",
        "description": "Provides information about the year wise area under food crops and non-food crops from 2001-2001 to 2016-2017.",
        "tags": [
          "open data",
          "AgriCredit",
          "district",
          "crop",
          "subdistrict",
          "agriculture",
          "land"
        ],
        "accessPolicy": "OPEN",
        "apdURL": "acl-apd.adex.org.in",
        "provider": "fe6e514e-8260-4ab2-bc9f-a26c8a32a216",
        "resourceServer": "41bb4389-ebaf-4df7-a575-556ec6092a25",
        "resourceGroup": "59c2af71-9661-4fac-94b3-45935781a7b6",
        "resourceType": "DATASET",
        "adexResourceAPIs": [
          "ATTR"
        ],
        "iudxResourceAPIs": [
          "ATTR"
        ],
        "dataDescriptor": {
          "@context": "https://agrijson.adex.org.in/",
          "type": [
            "iudx:DataDescriptor",
            "iudx:LandParcel",
            "adex:DataDescriptor",
            "adex:LandParcel"
          ],
          "dataDescriptorLabel": "Data Descriptor of Year Wise Trend Of Food Crops in Telangana State",
          "description": "Data attribute details provides information about the year wise area under food crops and non-food crops from 2001-2001 to 2016-2017.",
          "year": {
            "description": "The begining year of the survey or assement corresponding to this observation and is described in YYYY format, for eg. 2020.",
            "dataSchema": "adex:Number",
            "type": [
              "ValueDescriptor"
            ]
          },
          "evaluationYear": {
            "description": "The period during which a survey or assessment has been carried out.",
            "dataSchema": "adex:Text",
            "type": [
              "ValueDescriptor"
            ]
          },
          "cropArea": {
            "description": "Total area of the agricultural land used for cultivation, i.e, the arable land area.",
            "dataSchema": "adex:Number",
            "type": [
              "ValueDescriptor"
            ]
          },
          "foodCropArea": {
            "description": "The total area of land used solely for the cultivation of food crops (eg., rice, wheat, millets, etc.), excluding non-food crops (eg., cotton, rubber, etc). The land area under cultivation of non food crops can be derived from (cropArea-foodCropArea).",
            "dataSchema": "adex:Number",
            "type": [
              "ValueDescriptor"
            ]
          }
        },
        "dataSample": {
          "year": 2001,
          "evaluationYear": "2001-02",
          "cropArea": 4801150,
          "foodCropArea": 3398955
        },
        "location": {
          "type": "Place",
          "address": "Telangana",
          "geometry": {
            "coordinates": [
              [
                [
                  77.120821,
                  19.704752
                ],
                [
                  81.273653,
                  19.839154
                ],
                [
                  81.343529,
                  15.976888
                ],
                [
                  77.160163,
                  15.818332
                ],
                [
                  77.120821,
                  19.704752
                ]
              ]
            ],
            "type": "Polygon"
          }
        },
        "itemStatus": "ACTIVE",
        "ownerUserId": "6bdfa780-d8c0-4b2a-9a89-a1586d1d752f",
        "cos": "49f96c4c-e595-4fee-984c-43dededfba48",
        "itemCreatedAt": "2024-04-01T01:05:48+0530"
      },
      {
        "@context": "https://voc.iudx.org.in/",
        "type": [
          "iudx:Resource",
          "iudx:PowerDistribution",
          "adex:Resource",
          "adex:PowerDistribution"
        ],
        "id": "1ce8d434-88b4-4321-af8a-37244a6e5048",
        "name": "tg-npdcl-agriculture-consumption-data",
        "label": "NPDCL Agriculture Consumption Data in Telangana",
        "description": "Publishes information regarding agriculture consumption details in the northern part of Telangana on monthly basis.",
        "tags": [
          "open data",
          "AgriCredit",
          "district",
          "crop",
          "subdistrict",
          "agriculture",
          "land"
        ],
        "accessPolicy": "OPEN",
        "apdURL": "acl-apd.adex.org.in",
        "provider": "fe6e514e-8260-4ab2-bc9f-a26c8a32a216",
        "resourceServer": "41bb4389-ebaf-4df7-a575-556ec6092a25",
        "resourceGroup": "72ee13c0-b037-438c-8dea-3fe2a6bb7869",
        "resourceType": "MESSAGESTREAM",
        "adexResourceAPIs": [
          "TEMPORAL",
          "ATTR"
        ],
        "iudxResourceAPIs": [
          "TEMPORAL",
          "ATTR"
        ],
        "dataArrivalInterval": "Every start of the month",
        "dataDescriptor": {
          "@context": "https://agrijson.adex.org.in/",
          "type": [
            "iudx:DataDescriptor",
            "iudx:LandParcel",
            "adex:DataDescriptor",
            "adex:LandParcel"
          ],
          "dataDescriptorLabel": "Data Descriptor of NPDCL Agriculture Consumption Data in Telangana State",
          "description": "Data attribute details provides information about the agriculture consumption details in the northern part of Telangana.",
          "cityName": {
            "description": "Name of the city corresponding to this observation",
            "dataSchema": "adex:Number",
            "type": [
              "ValueDescriptor"
            ]
          },
          "powerDistributionDivision": {
            "description": "The name of the power distribution division corresponding to this observation.",
            "dataSchema": "adex:Number",
            "type": [
              "ValueDescriptor"
            ]
          },
          "powerDistributionSubdivision": {
            "description": "The name of the sub division in the power distribution corresponding to this observation.",
            "dataSchema": "adex:Text",
            "type": [
              "ValueDescriptor"
            ]
          },
          "powerDistributionSection": {
            "description": "The name of the section in the power distribution corresponding to this observation.",
            "dataSchema": "adex:Text",
            "type": [
              "ValueDescriptor"
            ]
          },
          "areaServed": {
            "description": "Area served by power distribution that corresponds to this observation.",
            "dataSchema": "adex:Text",
            "type": [
              "ValueDescriptor"
            ]
          },
          "category": {
            "description": "Type of power connection corresponding to this observation.",
            "dataSchema": "adex:Text",
            "type": [
              "ValueDescriptor"
            ]
          },
          "categoryCode": {
            "description": "The code of the category corresponding to this observation.",
            "dataSchema": "adex:Number",
            "type": [
              "ValueDescriptor"
            ]
          },
          "totalServiceCount": {
            "description": "The total count of services availed corresponding to this observation.",
            "dataSchema": "adex:Number",
            "type": [
              "ValueDescriptor"
            ]
          },
          "billedServicesCount": {
            "description": "The total count of services that are billed corresponding to this observation.",
            "dataSchema": "adex:Number",
            "type": [
              "ValueDescriptor"
            ]
          },
          "energyConsumption": {
            "description": "Energy consumed over a specific time corresponding to this observation.",
            "dataSchema": "adex:Number",
            "type": [
              "ValueDescriptor"
            ]
          },
          "powerConsumption": {
            "description": "The amount of power consumed corresponding to this observation.",
            "dataSchema": "adex:Number",
            "type": [
              "ValueDescriptor"
            ]
          },
          "date": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "Date corresponding to this observation and is described in YYYY-MM-DD format, for eg. '2020-11-05'.",
            "dataSchema": "iudx:Text"
          },
          "observationDateTime": {
            "description": "Last reported time of observation.",
            "dataSchema": "adex:DateTime",
            "type": [
              "ValueDescriptor"
            ]
          }
        },
        "dataSample": {
          "cityName": "KARIMNAGAR",
          "powerDistributionDivision": "KARIMNAGAR RURAL",
          "powerDistributionSubdivision": "NUSTHULAPUR",
          "powerDistributionSection": "NUTSULAPOOR",
          "areaServed": "RENIKUNTA",
          "category": "Agriculture",
          "categoryCode": 4,
          "totalServiceCount": 550,
          "billedServicesCount": 0,
          "energyConsumption": 0.0,
          "powerConsumption": 2601.0,
          "date": "2023-07-14",
          "observationDateTime": "2023-07-14T00:00:00+05:30"
        },
        "location": {
          "type": "Place",
          "address": "Telangana",
          "geometry": {
            "coordinates": [
              [
                [
                  77.120821,
                  19.704752
                ],
                [
                  81.273653,
                  19.839154
                ],
                [
                  81.343529,
                  15.976888
                ],
                [
                  77.160163,
                  15.818332
                ],
                [
                  77.120821,
                  19.704752
                ]
              ]
            ],
            "type": "Polygon"
          }
        },
        "itemStatus": "ACTIVE",
        "ownerUserId": "6bdfa780-d8c0-4b2a-9a89-a1586d1d752f",
        "cos": "49f96c4c-e595-4fee-984c-43dededfba48",
        "itemCreatedAt": "2024-04-01T01:05:52+0530"
      },
      {
        "@context": "https://voc.iudx.org.in/",
        "type": [
          "iudx:Resource",
          "iudx:PowerDistribution",
          "adex:Resource",
          "adex:PowerDistribution"
        ],
        "id": "ffd89bde-9abc-4dfd-a9d4-e8c3acce6d84",
        "name": "tg-spdcl-agriculture-consumption-data",
        "label": "SPDCL Agriculture Consumption Data in Telangana",
        "description": "Provides information about the agriculture consumption details in the southern part of Telangana on monthly basis.",
        "tags": [
          "open data",
          "AgriCredit",
          "district",
          "crop",
          "subdistrict",
          "agriculture",
          "land"
        ],
        "accessPolicy": "OPEN",
        "apdURL": "acl-apd.adex.org.in",
        "provider": "fe6e514e-8260-4ab2-bc9f-a26c8a32a216",
        "resourceServer": "41bb4389-ebaf-4df7-a575-556ec6092a25",
        "resourceGroup": "72ee13c0-b037-438c-8dea-3fe2a6bb7869",
        "resourceType": "MESSAGESTREAM",
        "adexResourceAPIs": [
          "TEMPORAL",
          "ATTR"
        ],
        "iudxResourceAPIs": [
          "TEMPORAL",
          "ATTR"
        ],
        "dataArrivalInterval": "Every start of the month",
        "dataDescriptor": {
          "@context": "https://agrijson.adex.org.in/",
          "type": [
            "iudx:DataDescriptor",
            "iudx:LandParcel",
            "adex:DataDescriptor",
            "adex:LandParcel"
          ],
          "dataDescriptorLabel": "Data Descriptor of SPDCL Agriculture Consumption Data in Telangana State",
          "description": "Data attribute details provides information about the agriculture consumption details in the southern part of Telangana.",
          "cityName": {
            "description": "Name of the city corresponding to this observation",
            "dataSchema": "adex:Number",
            "type": [
              "ValueDescriptor"
            ]
          },
          "powerDistributionDivision": {
            "description": "The name of the power distribution division corresponding to this observation.",
            "dataSchema": "adex:Number",
            "type": [
              "ValueDescriptor"
            ]
          },
          "powerDistributionSubdivision": {
            "description": "The name of the sub division in the power distribution corresponding to this observation.",
            "dataSchema": "adex:Text",
            "type": [
              "ValueDescriptor"
            ]
          },
          "powerDistributionSection": {
            "description": "The name of the section in the power distribution corresponding to this observation.",
            "dataSchema": "adex:Text",
            "type": [
              "ValueDescriptor"
            ]
          },
          "areaServed": {
            "description": "Area served by power distribution that corresponds to this observation.",
            "dataSchema": "adex:Text",
            "type": [
              "ValueDescriptor"
            ]
          },
          "category": {
            "description": "Type of power connection corresponding to this observation.",
            "dataSchema": "adex:Text",
            "type": [
              "ValueDescriptor"
            ]
          },
          "categoryCode": {
            "description": "The code of the category corresponding to this observation.",
            "dataSchema": "adex:Number",
            "type": [
              "ValueDescriptor"
            ]
          },
          "totalServiceCount": {
            "description": "The total count of services availed corresponding to this observation.",
            "dataSchema": "adex:Number",
            "type": [
              "ValueDescriptor"
            ]
          },
          "billedServicesCount": {
            "description": "The total count of services that are billed corresponding to this observation.",
            "dataSchema": "adex:Number",
            "type": [
              "ValueDescriptor"
            ]
          },
          "energyConsumption": {
            "description": "Energy consumed over a specific time corresponding to this observation.",
            "dataSchema": "adex:Number",
            "type": [
              "ValueDescriptor"
            ]
          },
          "powerConsumption": {
            "description": "The amount of power consumed corresponding to this observation.",
            "dataSchema": "adex:Number",
            "type": [
              "ValueDescriptor"
            ]
          },
          "date": {
            "type": [
              "ValueDescriptor"
            ],
            "description": "Date corresponding to this observation and is described in YYYY-MM-DD format, for eg. '2020-11-05'.",
            "dataSchema": "iudx:Text"
          },
          "observationDateTime": {
            "description": "Last reported time of observation.",
            "dataSchema": "adex:DateTime",
            "type": [
              "ValueDescriptor"
            ]
          }
        },
        "dataSample": {
          "cityName": "KARIMNAGAR",
          "powerDistributionDivision": "KARIMNAGAR RURAL",
          "powerDistributionSubdivision": "NUSTHULAPUR",
          "powerDistributionSection": "NUTSULAPOOR",
          "areaServed": "RENIKUNTA",
          "category": "Agriculture",
          "categoryCode": 4,
          "totalServiceCount": 550,
          "billedServicesCount": 0,
          "energyConsumption": 0.0,
          "powerConsumption": 2601.0,
          "date": "2023-07-14",
          "observationDateTime": "2023-07-14T00:00:00+05:30"
        },
        "location": {
          "type": "Place",
          "address": "Telangana",
          "geometry": {
            "coordinates": [
              [
                [
                  77.120821,
                  19.704752
                ],
                [
                  81.273653,
                  19.839154
                ],
                [
                  81.343529,
                  15.976888
                ],
                [
                  77.160163,
                  15.818332
                ],
                [
                  77.120821,
                  19.704752
                ]
              ]
            ],
            "type": "Polygon"
          }
        },
        "itemStatus": "ACTIVE",
        "ownerUserId": "6bdfa780-d8c0-4b2a-9a89-a1586d1d752f",
        "cos": "49f96c4c-e595-4fee-984c-43dededfba48",
        "itemCreatedAt": "2024-04-01T01:05:56+0530"
      }]



      
desired_keys = [
    "@context", "id", "type",  "name", "label", "description", "tags", "accessPolicy", "apdURL",
    "provider", "resourceServer", "resourceGroup", "resourceType", "iudxResourceAPIs",
    "dataArrivalInterval", "dataDescriptor", "dataSample", "dataSampleFile", "location",
    "itemStatus", "instance", "ownerUserId", "cos", "itemCreatedAt"
]


def extract_desired_keys(desired_keys, json_data):
    
    return {key: json_data[key] for key in desired_keys if json_data.get(key)}


json_new = []
for json_data in vv:
    json_data.pop("id_bck", None)  # Remove "id_bck" if present
    json_data.pop("provider_bck", None)  # Remove "provider_bck" if present
    json_data.pop("resourceGroup_bck", None)  # Remove "resourceGroup_bck" if present
    if json_data.get("iudxResourceAPIs", None):
        if "TEMPORAL" in json_data["iudxResourceAPIs"]:
            json_data["dataArrivalInterval"] = "Temporal"
        elif "TEMPORAL" not in json_data["iudxResourceAPIs"] and "ATTR" in json_data["iudxResourceAPIs"]:
            json_data["dataArrivalInterval"] = "NonTemporal"

    json_new.append(extract_desired_keys(desired_keys, json_data))
        
import json
with open("kjkj.json", "w") as file:
    json.dump(json_new, file, indent=5)