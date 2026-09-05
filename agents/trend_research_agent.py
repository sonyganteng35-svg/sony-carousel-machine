import json
import os
from datetime import datetime


print("🔥 Trend Research Agent Started")


trends = {

    "date":
    datetime.now().strftime("%Y-%m-%d"),


    "sources":[

        {
            "platform":"TikTok",
            "topic":
            "AI editing workflow",

            "reason":
            "Creator mencari cara edit lebih cepat"
        },


        {
            "platform":"Instagram",
            "topic":
            "Carousel edukasi saveable",

            "reason":
            "Konten edukasi meningkatkan authority"
        },


        {
            "platform":"CapCut",
            "topic":
            "AI template dan editing mobile",

            "reason":
            "Pemula ingin hasil profesional dengan HP"
        },


        {
            "platform":"UMKM",
            "topic":
            "Video produk smartphone",

            "reason":
            "Seller membutuhkan konten iklan murah"
        }

    ]

}


os.makedirs(
    "output",
    exist_ok=True
)


with open(
    "output/trend_research.json",
    "w"
) as f:

    json.dump(
        trends,
        f,
        indent=2
    )


print("✅ Trend research completed")
