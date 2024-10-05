import json
from time import process_time_ns
from traceback import print_tb
from validator import logValidator
x = {
    "created": [
        {
            "id": 4294967619,
            "props": {
                "role": "text",
                "text": [
                    "❮ Back"
                ]
            },
            "traits": {
                "compoundComponent": {
                    "mergeDescendants": False
                },
                "visibility": {
                    "alpha": 100,
                    "bounds": [
                        "(14,16)",
                        "(72,16)",
                        "(72,43)",
                        "(14,43)"
                    ]
                }
            }
        },
        {
            "id": 4294967618,
            "props": {
                "role": "button"
            },
            "traits": {
                "compoundComponent": {
                    "mergeDescendants": True
                },
                "focusable": {
                    "focused": False,
                    "setFocus": 640
                },
                "tappable": {
                    "handler": 639
                },
                "visibility": {
                    "alpha": 100,
                    "bounds": [
                        "(8,4)",
                        "(94,4)",
                        "(94,63)",
                        "(8,63)"
                    ],
                    "zIndex": 1000
                },
                "voiceAssistant": {
                    "entityType": "AMAZON.Thing"
                }
            }
        },
        {
            "id": 4294967617,
            "props": {
                "role": "text",
                "text": [
                    "minutes1 : 20"
                ]
            },
            "traits": {
                "compoundComponent": {
                    "mergeDescendants": False
                },
                "visibility": {
                    "alpha": 100,
                    "bounds": [
                        "(14,256)",
                        "(1636,256)",
                        "(1636,275)",
                        "(14,275)"
                    ]
                }
            }
        },
        {
            "id": 4294967616,
            "props": {
                "role": "text",
                "text": [
                    "hours1 : 14"
                ]
            },
            "traits": {
                "compoundComponent": {
                    "mergeDescendants": False
                },
                "visibility": {
                    "alpha": 100,
                    "bounds": [
                        "(14,233)",
                        "(1636,233)",
                        "(1636,252)",
                        "(14,252)"
                    ]
                }
            }
        },
        {
            "id": 4294967615,
            "props": {
                "role": "text",
                "text": [
                    "month1 : 7"
                ]
            },
            "traits": {
                "compoundComponent": {
                    "mergeDescendants": False
                },
                "visibility": {
                    "alpha": 100,
                    "bounds": [
                        "(14,210)",
                        "(1636,210)",
                        "(1636,229)",
                        "(14,229)"
                    ]
                }
            }
        },
        {
            "id": 4294967614,
            "props": {
                "role": "text",
                "text": [
                    "year1 : 1940"
                ]
            },
            "traits": {
                "compoundComponent": {
                    "mergeDescendants": False
                },
                "visibility": {
                    "alpha": 100,
                    "bounds": [
                        "(14,187)",
                        "(1636,187)",
                        "(1636,206)",
                        "(14,206)"
                    ]
                }
            }
        },
        {
            "id": 4294967613,
            "props": {
                "role": "text",
                "text": [
                    "date : \"1940, 7, 16, 14, 20, 10\""
                ]
            },
            "traits": {
                "compoundComponent": {
                    "mergeDescendants": False
                },
                "visibility": {
                    "alpha": 100,
                    "bounds": [
                        "(14,164)",
                        "(1636,164)",
                        "(1636,183)",
                        "(14,183)"
                    ]
                }
            }
        },
        {
            "id": 4294967612,
            "props": {
                "role": "text",
                "text": [
                    "option : {\"weekday\":\"long\",\"era\":\"short\",\"year\":\"numeric\",\"month\":\"long\",\"day\":\"numeric\",\"dayPeriod\":\"long\",\"calendar\":\"gregory\",\"numberingSystem\":\"mathsans\",\"hour\":\"2-digit\",\"minute\":\"2-digit\",\"second\":\"2-digit\",\"fractionalSecondDigits\":2,\"hourCycle\":\"h12\",\"timeZone\":\"Asia/Kolkata\",\"timeZoneName\":\"long\",\"formatMatcher\":\"basic\",\"hour12\":True}"
                ]
            },
            "traits": {
                "compoundComponent": {
                    "mergeDescendants": False
                },
                "visibility": {
                    "alpha": 100,
                    "bounds": [
                        "(14,122)",
                        "(1636,122)",
                        "(1636,160)",
                        "(14,160)"
                    ]
                }
            }
        },
        {
            "id": 4294967611,
            "props": {
                "role": "text",
                "text": [
                    "locale : \"en-US\""
                ]
            },
            "traits": {
                "compoundComponent": {
                    "mergeDescendants": False
                },
                "visibility": {
                    "alpha": 100,
                    "bounds": [
                        "(14,99)",
                        "(1636,99)",
                        "(1636,118)",
                        "(14,118)"
                    ]
                }
            }
        },
        {
            "id": 4294967610,
            "props": {
                "role": "text",
                "text": [
                    "Input : "
                ]
            },
            "traits": {
                "compoundComponent": {
                    "mergeDescendants": False
                },
                "visibility": {
                    "alpha": 100,
                    "bounds": [
                        "(14,76)",
                        "(1636,76)",
                        "(1636,95)",
                        "(14,95)"
                    ]
                }
            }
        },
        {
            "id": 4294967609,
            "props": {
                "role": "text",
                "text": [
                    "formatToParts()"
                ]
            },
            "traits": {
                "compoundComponent": {
                    "mergeDescendants": False
                },
                "visibility": {
                    "alpha": 100,
                    "bounds": [
                        "(14,18)",
                        "(1636,18)",
                        "(1636,40)",
                        "(14,40)"
                    ]
                }
            }
        },
        {
            "id": 4294967608,
            "traits": {
                "compoundComponent": {
                    "mergeDescendants": False
                },
                "visibility": {
                    "alpha": 100,
                    "bounds": [
                        "(0,0)",
                        "(1650,0)",
                        "(1650,58)",
                        "(0,58)"
                    ]
                }
            }
        },
        {
            "id": 4294967607,
            "traits": {
                "compoundComponent": {
                    "mergeDescendants": False
                },
                "visibility": {
                    "alpha": 100,
                    "bounds": [
                        "(0,569)",
                        "(1650,569)",
                        "(1650,1023)",
                        "(0,1023)"
                    ]
                }
            }
        },
        {
            "id": 4294967606,
            "props": {
                "role": "text",
                "text": [
                    "Thursday, 𝟣𝟦 May 𝟤𝟢𝟤𝟢 Anno Domini, 𝟢𝟤:𝟢𝟢:𝟣𝟤.𝟢𝟢 in the afternoon IST"
                ]
            },
            "traits": {
                "compoundComponent": {
                    "mergeDescendants": False
                },
                "visibility": {
                    "alpha": 100,
                    "bounds": [
                        "(14,509)",
                        "(1636,509)",
                        "(1636,531)",
                        "(14,531)"
                    ]
                }
            }
        },
        {
            "id": 4294967605,
            "props": {
                "role": "text",
                "text": [
                    "Tue, 𝟪 May 𝟤𝟢𝟣𝟤 Anno Domini, 𝟢𝟧:𝟥𝟢:𝟢𝟢.𝟢𝟢 at night IST"
                ]
            },
            "traits": {
                "compoundComponent": {
                    "mergeDescendants": False
                },
                "visibility": {
                    "alpha": 100,
                    "bounds": [
                        "(14,483)",
                        "(1636,483)",
                        "(1636,505)",
                        "(14,505)"
                    ]
                }
            }
        },
        {
            "id": 4294967588,
            "props": {
                "role": "text",
                "text": [
                    "format()"
                ]
            },
            "traits": {
                "compoundComponent": {
                    "mergeDescendants": False
                },
                "visibility": {
                    "alpha": 100,
                    "bounds": [
                        "(14,18)",
                        "(1636,18)",
                        "(1636,40)",
                        "(14,40)"
                    ]
                }
            }
        },
        {
            "id": 4294967587,
            "traits": {
                "compoundComponent": {
                    "mergeDescendants": False
                },
                "visibility": {
                    "alpha": 100,
                    "bounds": [
                        "(0,0)",
                        "(1650,0)",
                        "(1650,58)",
                        "(0,58)"
                    ]
                }
            }
        },
        {
            "id": 4294967586,
            "traits": {
                "compoundComponent": {
                    "mergeDescendants": False
                },
                "visibility": {
                    "alpha": 100,
                    "bounds": [
                        "(0,0)",
                        "(1650,0)",
                        "(1650,549)",
                        "(0,549)"
                    ]
                }
            }
        },
        {
            "id": 4294967585,
            "traits": {
                "compoundComponent": {
                    "mergeDescendants": False
                },
                "visibility": {
                    "alpha": 100,
                    "bounds": [
                        "(0,0)",
                        "(1650,0)",
                        "(1650,2759)",
                        "(0,2759)"
                    ]
                }
            }
        },
        {
            "id": 4294967584,
            "traits": {
                "focusable": {
                    "focused": False,
                    "setFocus": 637
                },
                "scrollable": {
                    "directions": [
                        "down"
                    ],
                    "offset": "(0,0)",
                    "pageFunction": 636
                },
                "visibility": {
                    "bounds": [
                        "(0,0)",
                        "(1650,0)",
                        "(1650,838)",
                        "(0,838)"
                    ]
                }
            }
        },
        {
            "id": 4294967583,
            "traits": {
                "visibility": {
                    "bounds": [
                        "(5,178)",
                        "(1655,178)",
                        "(1655,1016)",
                        "(5,1016)"
                    ]
                }
            }
        },
        {
            "id": 4294967582,
            "props": {
                "role": "text",
                "text": [
                    "// This feature is only available on Kepler devices. It is not supported on KeplerBridge or other devices."
                ]
            },
            "traits": {
                "compoundComponent": {
                    "mergeDescendants": False
                },
                "visibility": {
                    "alpha": 100,
                    "bounds": [
                        "(14,41)",
                        "(1636,41)",
                        "(1636,60)",
                        "(14,60)"
                    ]
                }
            }
        },
        {
            "id": 4294967581,
            "props": {
                "role": "text",
                "text": [
                    "Intl.DateTimeFormat : available"
                ]
            },
            "traits": {
                "compoundComponent": {
                    "mergeDescendants": False
                },
                "visibility": {
                    "alpha": 100,
                    "bounds": [
                        "(14,18)",
                        "(1636,18)",
                        "(1636,37)",
                        "(14,37)"
                    ]
                }
            }
        },
        {
            "id": 4294967580,
            "traits": {
                "compoundComponent": {
                    "mergeDescendants": False
                },
                "visibility": {
                    "alpha": 100,
                    "bounds": [
                        "(5,80)",
                        "(1655,80)",
                        "(1655,158)",
                        "(5,158)"
                    ]
                }
            }
        },
        {
            "id": 4294967579,
            "props": {
                "role": "text",
                "text": [
                    "Intl.DateTimeFormat Demo"
                ]
            },
            "traits": {
                "compoundComponent": {
                    "mergeDescendants": False
                },
                "visibility": {
                    "alpha": 100,
                    "bounds": [
                        "(14,18)",
                        "(262,18)",
                        "(262,42)",
                        "(14,42)"
                    ]
                }
            }
        },
        {
            "id": 4294967578,
            "traits": {
                "compoundComponent": {
                    "mergeDescendants": False
                },
                "visibility": {
                    "alpha": 100,
                    "bounds": [
                        "(692,0)",
                        "(968,0)",
                        "(968,60)",
                        "(692,60)"
                    ]
                }
            }
        },
        {
            "id": 4294967577,
            "traits": {
                "compoundComponent": {
                    "mergeDescendants": False
                },
                "visibility": {
                    "alpha": 100,
                    "bounds": [
                        "(5,64)",
                        "(1665,64)",
                        "(1665,1080)",
                        "(5,1080)"
                    ]
                }
            }
        },
        {
            "id": 4294967576,
            "props": {
                "role": "text",
                "text": [
                    "DateTimeFormat"
                ]
            },
            "traits": {
                "compoundComponent": {
                    "mergeDescendants": False
                },
                "visibility": {
                    "alpha": 100,
                    "bounds": [
                        "(712,0)",
                        "(958,0)",
                        "(958,64)",
                        "(712,64)"
                    ]
                }
            }
        },
        {
            "id": 4294967589,
            "props": {
                "role": "text",
                "text": [
                    "Input : "
                ]
            },
            "traits": {
                "compoundComponent": {
                    "mergeDescendants": False
                },
                "visibility": {
                    "alpha": 100,
                    "bounds": [
                        "(14,76)",
                        "(1636,76)",
                        "(1636,95)",
                        "(14,95)"
                    ]
                }
            }
        },
        {
            "id": 4294967590,
            "props": {
                "role": "text",
                "text": [
                    "locale : [\"en-IN\"]"
                ]
            },
            "traits": {
                "compoundComponent": {
                    "mergeDescendants": False
                },
                "visibility": {
                    "alpha": 100,
                    "bounds": [
                        "(14,99)",
                        "(1636,99)",
                        "(1636,118)",
                        "(14,118)"
                    ]
                }
            }
        },
        {
            "id": 4294967591,
            "props": {
                "role": "text",
                "text": [
                    "option : {\"weekday\":\"long\",\"era\":\"long\",\"year\":\"numeric\",\"month\":\"long\",\"day\":\"numeric\",\"dayPeriod\":\"short\",\"localeMatcher\":\"best fit\",\"calendar\":\"gregory\",\"numberingSystem\":\"mathsans\",\"hour\":\"2-digit\",\"minute\":\"2-digit\",\"second\":\"2-digit\",\"fractionalSecondDigits\":2,\"hourCycle\":\"h12\",\"timeZone\":\"Asia/Kolkata\",\"timeZoneName\":\"short\",\"formatMatcher\":\"basic\",\"hour12\":True}"
                ]
            },
            "traits": {
                "compoundComponent": {
                    "mergeDescendants": False
                },
                "visibility": {
                    "alpha": 100,
                    "bounds": [
                        "(14,122)",
                        "(1636,122)",
                        "(1636,160)",
                        "(14,160)"
                    ]
                }
            }
        },
        {
            "id": 4294967592,
            "props": {
                "role": "text",
                "text": [
                    "date1 : \"2012-05-08T00:00:00.000Z\""
                ]
            },
            "traits": {
                "compoundComponent": {
                    "mergeDescendants": False
                },
                "visibility": {
                    "alpha": 100,
                    "bounds": [
                        "(14,164)",
                        "(1636,164)",
                        "(1636,183)",
                        "(14,183)"
                    ]
                }
            }
        },
        {
            "id": 4294967593,
            "props": {
                "role": "text",
                "text": [
                    "date2 : \"2020, 4, 14, 12, 30, 40\""
                ]
            },
            "traits": {
                "compoundComponent": {
                    "mergeDescendants": False
                },
                "visibility": {
                    "alpha": 100,
                    "bounds": [
                        "(14,187)",
                        "(1636,187)",
                        "(1636,206)",
                        "(14,206)"
                    ]
                }
            }
        },
        {
            "id": 4294967594,
            "props": {
                "role": "text",
                "text": [
                    "year2 : 2020"
                ]
            },
            "traits": {
                "compoundComponent": {
                    "mergeDescendants": False
                },
                "visibility": {
                    "alpha": 100,
                    "bounds": [
                        "(14,210)",
                        "(1636,210)",
                        "(1636,229)",
                        "(14,229)"
                    ]
                }
            }
        },
        {
            "id": 4294967595,
            "props": {
                "role": "text",
                "text": [
                    "month2 : 4"
                ]
            },
            "traits": {
                "compoundComponent": {
                    "mergeDescendants": False
                },
                "visibility": {
                    "alpha": 100,
                    "bounds": [
                        "(14,233)",
                        "(1636,233)",
                        "(1636,252)",
                        "(14,252)"
                    ]
                }
            }
        },
        {
            "id": 4294967596,
            "props": {
                "role": "text",
                "text": [
                    "hours2 : 12"
                ]
            },
            "traits": {
                "compoundComponent": {
                    "mergeDescendants": False
                },
                "visibility": {
                    "alpha": 100,
                    "bounds": [
                        "(14,256)",
                        "(1636,256)",
                        "(1636,275)",
                        "(14,275)"
                    ]
                }
            }
        },
        {
            "id": 4294967597,
            "props": {
                "role": "text",
                "text": [
                    "minutes2 : 30"
                ]
            },
            "traits": {
                "compoundComponent": {
                    "mergeDescendants": False
                },
                "visibility": {
                    "alpha": 100,
                    "bounds": [
                        "(14,279)",
                        "(1636,279)",
                        "(1636,298)",
                        "(14,298)"
                    ]
                }
            }
        },
        {
            "id": 4294967598,
            "props": {
                "role": "text",
                "text": [
                    "seconds2 : 12"
                ]
            },
            "traits": {
                "compoundComponent": {
                    "mergeDescendants": False
                },
                "visibility": {
                    "alpha": 100,
                    "bounds": [
                        "(14,302)",
                        "(1636,302)",
                        "(1636,321)",
                        "(14,321)"
                    ]
                }
            }
        },
        {
            "id": 4294967599,
            "props": {
                "role": "text",
                "text": [
                    "Implementation : "
                ]
            },
            "traits": {
                "compoundComponent": {
                    "mergeDescendants": False
                },
                "visibility": {
                    "alpha": 100,
                    "bounds": [
                        "(14,335)",
                        "(1636,335)",
                        "(1636,354)",
                        "(14,354)"
                    ]
                }
            }
        },
        {
            "id": 4294967600,
            "props": {
                "role": "text",
                "text": [
                    "output1 : new Intl.DateTimeFormat(locale, option).format(date1)"
                ]
            },
            "traits": {
                "compoundComponent": {
                    "mergeDescendants": False
                },
                "visibility": {
                    "alpha": 100,
                    "bounds": [
                        "(14,358)",
                        "(1636,358)",
                        "(1636,377)",
                        "(14,377)"
                    ]
                }
            }
        },
        {
            "id": 4294967601,
            "props": {
                "role": "text",
                "text": [
                    "output2 : new Intl.DateTimeFormat(locale, option).format(new Date(year2, month2, day2, hours2, minutes2, seconds2))"
                ]
            },
            "traits": {
                "compoundComponent": {
                    "mergeDescendants": False
                },
                "visibility": {
                    "alpha": 100,
                    "bounds": [
                        "(14,381)",
                        "(1636,381)",
                        "(1636,400)",
                        "(14,400)"
                    ]
                }
            }
        },
        {
            "id": 4294967602,
            "props": {
                "role": "text",
                "text": [
                    "console.log(output1)"
                ]
            },
            "traits": {
                "compoundComponent": {
                    "mergeDescendants": False
                },
                "visibility": {
                    "alpha": 100,
                    "bounds": [
                        "(14,404)",
                        "(1636,404)",
                        "(1636,423)",
                        "(14,423)"
                    ]
                }
            }
        },
        {
            "id": 4294967603,
            "props": {
                "role": "text",
                "text": [
                    "console.log(output2)"
                ]
            },
            "traits": {
                "compoundComponent": {
                    "mergeDescendants": False
                },
                "visibility": {
                    "alpha": 100,
                    "bounds": [
                        "(14,427)",
                        "(1636,427)",
                        "(1636,446)",
                        "(14,446)"
                    ]
                }
            }
        },
        {
            "id": 4294967604,
            "props": {
                "role": "text",
                "text": [
                    "Output : "
                ]
            },
            "traits": {
                "compoundComponent": {
                    "mergeDescendants": False
                },
                "visibility": {
                    "alpha": 100,
                    "bounds": [
                        "(14,460)",
                        "(1636,460)",
                        "(1636,479)",
                        "(14,479)"
                    ]
                }
            }
        }
    ]
}

ref_data = {
    "app_name": "intl",
    "intl": {
        "formatOption": {
            "weekday": "long",
            "era": "long",
            "year": "numeric",
            "month": "long",
            "day": "numeric",
            "dayPeriod": "short",
            "localeMatcher": "best fit",
            "calendar": "gregory",
            "numberingSystem": "mathsans",
            "hour": "2-digit",
            "minute": "2-digit",
            "second": "2-digit",
            "fractionalSecondDigits": 2,
            "hourCycle": "h12",
            "timeZone": "Asia/Kolkata",
            "timeZoneName": "short",
            "formatMatcher": "basic",
            "hour12": True
        },
        "formatDate1": "2020-08-10",
        "formatDate2": "2026, 5, 18, 1, 40, 50",
        "formatLocales": [
            "en-IN"
        ],
        "resolvedOption": {
            "options": {
                "timeZone": "Australia/Brisbane"
            },
            "locales": "zh-CN"
        },
        "supportedLocalesOf": {
            "locales": [
                "ban",
                "id-u-co-pinyin",
                "de-ID",
                "hi",
                "da-Dk",
                "zh-Hans-CN"
            ],
            "options": {
                "localeMatcher": "lookup"
            }
        },
        "formatToPartsOption": {
            "weekday": "long",
            "era": "short",
            "year": "numeric",
            "month": "long",
            "day": "numeric",
            "dayPeriod": "long",
            "calendar": "gregory",
            "numberingSystem": "mathsans",
            "hour": "2-digit",
            "minute": "2-digit",
            "second": "2-digit",
            "fractionalSecondDigits": 2,
            "hourCycle": "h12",
            "timeZone": "Asia/Kolkata",
            "timeZoneName": "long",
            "formatMatcher": "basic",
            "hour12": True
        },
        "formatToPartsDate": "1940, 7, 16, 14, 20, 10",
        "formatToPartsLocales": "en-US",
        "formatRangeDateStart":"null",
        "formatRangeDateEnd":"2024, 1, 15, 11, 50, 0",
        "formatRangeOptions": {
            "locales": "en-GB",
            "options": {
                "era":"narrow",
		"dayPeriod":"long",
                "weekday": "short",
                "year": "numeric",
                "month": "numeric",
                "day": "2-digit",
		"hour": "2-digit",
                "minute": "2-digit",
		"timeZone": "Asia/Kolkata",
		"timeZoneName":"long"

            }
         },
        "formatRangeToPartsDateStart": "2010, 2, 15, 3, 30, 0",
	"formatRangeToPartsDateEnd": "undefined",
        "formatRangeToPartsOptions": {
            "locales": "en-US",
            "options": {
		"era":"narrow",
		"dayPeriod":"long",
                "weekday": "short",
                "year": "numeric",
                "month": "numeric",
                "day": "2-digit",
		"hour": "2-digit",
                "minute": "2-digit",
		"timeZone": "Asia/Kolkata",
		"timeZoneName":"long"
            }
        },
        "relativeTimeFormatOption": {
            "locales": "en",
            "options": {
                "style": "short"
            }
        },
        "relativeTimeFormatTime": 3,
        "relativeTimeFormatUnit": "quarter",
        "relativeTimeFormatToPartsOption": {
            "locales": "en",
            "options": {
                "numeric": "auto"
            }
        },
        "relativeTimeFormatToPartsTime": 10,
        "relativeTimeFormatToPartsUnit": "seconds",
        "relativeTimeResolvedOption": {
            "locales": "en",
            "options": {
                "style": "narrow"
            }
        },
        "relativeTimeSupportedLocalesOf": {
            "locales": [
                "ban",
                "id-u-co-pinyin",
                "de-ID"
            ],
            "options": {
                "localeMatcher": "lookup"
            }
        }
    }
}


temp_data = list()
day_list = list()
for i in x['created']:
    if 'props' in i:
        if 'text' in i['props']:
            if 'IST' in i['props']['text'][0]:
                temp_data.append(i['props']['text'][0])
    else:
        pass
for j in temp_data:
    k = j.split(',')
    day_list.append(k[0])

for abc in day_list:
    xyz = logValidator(ref_data['intl']['formatOption']['weekday'],abc)
    print(xyz.weekdaysValidator())