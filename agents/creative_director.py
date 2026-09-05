import json


research = json.load(
    open("output/research_result.json")
)


creative_plan = {
    "brand": "Bos Sony Creative Studio",

    "strategy": {
        "audience": 
        "UMKM pemula dan creator yang ingin video terlihat profesional",

        "goal":
        "Membangun authority dan menarik calon klien jasa editing",

        "content_angle":
        "Edukasi praktis dengan pendekatan problem solving"
    },


    "carousel_ideas": [

        {
            "title":
            "3 Kesalahan Video Produk HP yang Bikin Orang Tidak Jadi Beli",

            "hook":
            "Video produk kamu terlihat murah? Masalahnya mungkin bukan kameranya.",

            "slides":[

                {
                "number":1,
                "headline":
                "HP mahal tidak menjamin video terlihat mahal",

                "purpose":
                "Stop scroll"
                },


                {
                "number":2,
                "headline":
                "Kesalahan pertama: Lighting asal",

                "purpose":
                "Membangun awareness masalah"
                },


                {
                "number":3,
                "headline":
                "Kesalahan kedua: Cuma ambil satu angle",

                "purpose":
                "Memberikan insight"
                },


                {
                "number":4,
                "headline":
                "Gunakan pola 4 shot sederhana",

                "purpose":
                "Memberikan solusi"
                },


                {
                "number":5,
                "headline":
                "Follow untuk belajar bikin video seperti iklan",

                "purpose":
                "Conversion"
                }

            ]
        }

    ]
}


with open(
    "output/creative_plan.json",
    "w"
) as f:

    json.dump(
        creative_plan,
        f,
        indent=2
    )


print("Creative Director finished")
