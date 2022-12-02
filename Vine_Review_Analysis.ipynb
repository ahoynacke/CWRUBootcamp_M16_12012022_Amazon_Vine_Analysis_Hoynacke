{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "dTMi5ZmRQEKe",
        "outputId": "c7d6249d-062c-4a71-dea0-1730967aea9e"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\r0% [Working]\r            \rGet:1 http://security.ubuntu.com/ubuntu bionic-security InRelease [88.7 kB]\n",
            "\r0% [Waiting for headers] [1 InRelease 14.2 kB/88.7 kB 16%] [Connected to cloud.\r                                                                               \rHit:2 http://archive.ubuntu.com/ubuntu bionic InRelease\n",
            "\r0% [Waiting for headers] [1 InRelease 88.7 kB/88.7 kB 100%] [Connected to cloud\r                                                                               \rGet:3 http://archive.ubuntu.com/ubuntu bionic-updates InRelease [88.7 kB]\n",
            "Get:4 https://cloud.r-project.org/bin/linux/ubuntu bionic-cran40/ InRelease [3,626 B]\n",
            "Hit:5 http://ppa.launchpad.net/c2d4u.team/c2d4u4.0+/ubuntu bionic InRelease\n",
            "Ign:6 https://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64  InRelease\n",
            "Get:7 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64  InRelease [1,581 B]\n",
            "Get:8 http://archive.ubuntu.com/ubuntu bionic-backports InRelease [83.3 kB]\n",
            "Hit:9 https://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64  Release\n",
            "Hit:10 http://ppa.launchpad.net/cran/libgit2/ubuntu bionic InRelease\n",
            "Hit:11 http://ppa.launchpad.net/deadsnakes/ppa/ubuntu bionic InRelease\n",
            "Get:12 http://ppa.launchpad.net/graphics-drivers/ppa/ubuntu bionic InRelease [21.3 kB]\n",
            "Get:13 http://security.ubuntu.com/ubuntu bionic-security/main amd64 Packages [3,094 kB]\n",
            "Get:14 http://security.ubuntu.com/ubuntu bionic-security/restricted amd64 Packages [1,294 kB]\n",
            "Get:15 http://security.ubuntu.com/ubuntu bionic-security/universe amd64 Packages [1,568 kB]\n",
            "Get:16 http://archive.ubuntu.com/ubuntu bionic-updates/restricted amd64 Packages [1,334 kB]\n",
            "Get:17 http://archive.ubuntu.com/ubuntu bionic-updates/main amd64 Packages [3,519 kB]\n",
            "Get:18 http://archive.ubuntu.com/ubuntu bionic-updates/universe amd64 Packages [2,342 kB]\n",
            "Get:19 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64  Packages [1,039 kB]\n",
            "Get:21 http://ppa.launchpad.net/graphics-drivers/ppa/ubuntu bionic/main amd64 Packages [38.5 kB]\n",
            "Fetched 14.5 MB in 8s (1,855 kB/s)\n",
            "Reading package lists... Done\n"
          ]
        }
      ],
      "source": [
        "import os\n",
        "# Find the latest version of spark 3.0 from http://www.apache.org/dist/spark/ and enter as the spark version\n",
        "# For example:\n",
        "# spark_version = 'spark-3.0.3'\n",
        "spark_version = 'spark-3.1.3'\n",
        "os.environ['SPARK_VERSION']=spark_version\n",
        "\n",
        "# Install Spark and Java\n",
        "!apt-get update\n",
        "!apt-get install openjdk-11-jdk-headless -qq > /dev/null\n",
        "!wget -q http://www.apache.org/dist/spark/$SPARK_VERSION/$SPARK_VERSION-bin-hadoop2.7.tgz\n",
        "!tar xf $SPARK_VERSION-bin-hadoop2.7.tgz\n",
        "!pip install -q findspark\n",
        "\n",
        "# Set Environment Variables\n",
        "import os\n",
        "os.environ[\"JAVA_HOME\"] = \"/usr/lib/jvm/java-11-openjdk-amd64\"\n",
        "os.environ[\"SPARK_HOME\"] = f\"/content/{spark_version}-bin-hadoop2.7\"\n",
        "\n",
        "# Start a SparkSession\n",
        "import findspark\n",
        "findspark.init()"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install pyspark"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "RxOqTVS8RKWq",
        "outputId": "f386a8d2-8ed7-41cf-92c7-cccf89b63660"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Looking in indexes: https://pypi.org/simple, https://us-python.pkg.dev/colab-wheels/public/simple/\n",
            "Collecting pyspark\n",
            "  Downloading pyspark-3.3.1.tar.gz (281.4 MB)\n",
            "\u001b[K     |████████████████████████████████| 281.4 MB 36 kB/s \n",
            "\u001b[?25hCollecting py4j==0.10.9.5\n",
            "  Downloading py4j-0.10.9.5-py2.py3-none-any.whl (199 kB)\n",
            "\u001b[K     |████████████████████████████████| 199 kB 20.2 MB/s \n",
            "\u001b[?25hBuilding wheels for collected packages: pyspark\n",
            "  Building wheel for pyspark (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "  Created wheel for pyspark: filename=pyspark-3.3.1-py2.py3-none-any.whl size=281845512 sha256=6572161a3ed1bcf40ce9d64fe4b9ddbbce1bcaeab2c969da06a41991fbcc21ca\n",
            "  Stored in directory: /root/.cache/pip/wheels/43/dc/11/ec201cd671da62fa9c5cc77078235e40722170ceba231d7598\n",
            "Successfully built pyspark\n",
            "Installing collected packages: py4j, pyspark\n",
            "Successfully installed py4j-0.10.9.5 pyspark-3.3.1\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!wget https://jdbc.postgresql.org/download/postgresql-42.2.16.jar"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "fGrY9406RNDN",
        "outputId": "844df4ea-63db-4117-e7d4-03b917a4d2f3"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "--2022-12-01 20:01:09--  https://jdbc.postgresql.org/download/postgresql-42.2.16.jar\n",
            "Resolving jdbc.postgresql.org (jdbc.postgresql.org)... 72.32.157.228, 2001:4800:3e1:1::228\n",
            "Connecting to jdbc.postgresql.org (jdbc.postgresql.org)|72.32.157.228|:443... connected.\n",
            "HTTP request sent, awaiting response... 200 OK\n",
            "Length: 1002883 (979K) [application/java-archive]\n",
            "Saving to: ‘postgresql-42.2.16.jar’\n",
            "\n",
            "postgresql-42.2.16. 100%[===================>] 979.38K  6.22MB/s    in 0.2s    \n",
            "\n",
            "2022-12-01 20:01:10 (6.22 MB/s) - ‘postgresql-42.2.16.jar’ saved [1002883/1002883]\n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from pyspark.sql import SparkSession\n",
        "spark = SparkSession.builder.appName(\"M16-Amazon-Challenge\").config(\"spark.driver.extraClassPath\",\"/content/postgresql-42.2.16.jar\").getOrCreate()"
      ],
      "metadata": {
        "id": "ymUwNZYLRQT0"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from pyspark import SparkFiles\n",
        "url = \"https://s3.amazonaws.com/amazon-reviews-pds/tsv/amazon_reviews_us_Furniture_v1_00.tsv.gz\"\n",
        "spark.sparkContext.addFile(url)\n",
        "df = spark.read.option(\"encoding\", \"UTF-8\").csv(SparkFiles.get(\"amazon_reviews_us_Furniture_v1_00.tsv.gz\"), sep=\"\\t\", header=True, inferSchema=True)\n",
        "df.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "elLauxOTRZxz",
        "outputId": "52b9ba05-485c-44ca-f06e-8c265595551c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "+-----------+-----------+--------------+----------+--------------+--------------------+----------------+-----------+-------------+-----------+----+-----------------+--------------------+--------------------+-----------+\n",
            "|marketplace|customer_id|     review_id|product_id|product_parent|       product_title|product_category|star_rating|helpful_votes|total_votes|vine|verified_purchase|     review_headline|         review_body|review_date|\n",
            "+-----------+-----------+--------------+----------+--------------+--------------------+----------------+-----------+-------------+-----------+----+-----------------+--------------------+--------------------+-----------+\n",
            "|         US|   24509695|R3VR960AHLFKDV|B004HB5E0E|     488241329|Shoal Creek Compu...|       Furniture|          4|            0|          0|   N|                Y|... desk is very ...|This desk is very...| 2015-08-31|\n",
            "|         US|   34731776|R16LGVMFKIUT0G|B0042TNMMS|     205864445|Dorel Home Produc...|       Furniture|          5|            0|          0|   N|                Y|          Five Stars|          Great item| 2015-08-31|\n",
            "|         US|    1272331|R1AIMEEPYHMOE4|B0030MPBZ4|     124663823|Bathroom Vanity T...|       Furniture|          5|            1|          1|   N|                Y|          Five Stars|Perfect fit for m...| 2015-08-31|\n",
            "|         US|   45284262|R1892CCSZWZ9SR|B005G02ESA|     382367578|Sleep Master Ulti...|       Furniture|          3|            0|          0|   N|                Y|         Good enough|We use this on a ...| 2015-08-31|\n",
            "|         US|   30003523|R285P679YWVKD1|B005JS8AUA|     309497463|1 1/4\" GashGuards...|       Furniture|          3|            0|          0|   N|                N|Gash Gards for da...|The product is fi...| 2015-08-31|\n",
            "|         US|   18311821| RLB33HJBXHZHU|B00AVUQQGQ|     574537906|Serta Bonded Leat...|       Furniture|          5|            0|          0|   N|                Y|          Five Stars|Love this product...| 2015-08-31|\n",
            "|         US|   42943632|R1VGTZ94DBAD6A|B00CFY20GQ|     407473883|Prepac Shoe Stora...|       Furniture|          5|            2|          2|   N|                Y|   I love this bench|I love this bench...| 2015-08-31|\n",
            "|         US|   43157304|R168KF82ICSOHD|B00FKC48QA|     435120460|HomCom PU Leather...|       Furniture|          5|            0|          0|   N|                Y|Great storage cap...|Have had this for...| 2015-08-31|\n",
            "|         US|   51918480|R20DIYIJ0OCMOG|B00N9IAL9K|     356495985|  Folding Step Stool|       Furniture|          5|            0|          0|   N|                Y|This is the best ...|This is the best ...| 2015-08-31|\n",
            "|         US|   14522766| RD46RNVOHNZSC|B001T4XU1C|     243050228|Ace Bayou Adult V...|       Furniture|          5|            0|          0|   N|                Y|    great for price!|    my son loves it!| 2015-08-31|\n",
            "|         US|   43054112|R2JDOCETTM3AXS|B002HRFLBC|      93574483|4D Concepts Audio...|       Furniture|          5|            0|          0|   N|                Y|          Five Stars|       Great product| 2015-08-31|\n",
            "|         US|   26622950|R33YMW36IDZ6LE|B006MISZOC|     941823468|Zinus SC-SBBK-14N...|       Furniture|          5|            0|          0|   N|                Y|             perfect|bought with sleep...| 2015-08-31|\n",
            "|         US|   17988940|R30ZGGUHZ04C1S|B008BMGABC|     460567746|Poundex Marble Di...|       Furniture|          5|            1|          1|   N|                Y|   Very satisfied!!!|Delivery was on t...| 2015-08-31|\n",
            "|         US|   18444952| RS2EZU76IK2BT|B00CO2VH5Y|     829613894|Safavieh Lyndhurs...|       Furniture|          5|            0|          0|   N|                Y|soft and great fo...|Exactly as pictur...| 2015-08-31|\n",
            "|         US|   16937084|R1GJC1BP028XO9|B00LI4RJQ0|     816478187|Sauder Boone Moun...|       Furniture|          5|            2|          3|   N|                Y|        Great table.|Beautiful table. ...| 2015-08-31|\n",
            "|         US|   23665632|R2VKJPGXXEK5GP|B0046EC1D0|     358594389|Winsome Wood Brea...|       Furniture|          1|            0|          0|   N|                Y|Not what I expect...|I have cleaned up...| 2015-08-31|\n",
            "|         US|    4110125|R17KS83G3KLT97|B00DQQPL36|     312571325|HODEDAH IMPORT Me...|       Furniture|          3|            0|          0|   N|                Y|         Three Stars|First one came in...| 2015-08-31|\n",
            "|         US|     107621|R3PQL8SR4NEHWL|B003X7RWB2|     402665054|Flash Furniture H...|       Furniture|          4|            0|          0|   N|                Y|          Four Stars|Good deal to get ...| 2015-08-31|\n",
            "|         US|    2415090|R2F5WW7WNO5RRG|B001TJYPJ8|     854989315|Sleep Revolution ...|       Furniture|          5|            0|          0|   N|                Y|          Five Stars|Comfortable and e...| 2015-08-31|\n",
            "|         US|   48285966|R3UDJKVWQCFIC9|B000TMHX9A|     814079288|Flash Furniture V...|       Furniture|          5|            0|          0|   N|                Y|Very comfortable....|As advertised. Ve...| 2015-08-31|\n",
            "+-----------+-----------+--------------+----------+--------------+--------------------+----------------+-----------+-------------+-----------+----+-----------------+--------------------+--------------------+-----------+\n",
            "only showing top 20 rows\n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "0RoxZMfXRbDT",
        "outputId": "d32ecfaa-b653-48c4-aa37-e933b2bd4a39"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "DataFrame[marketplace: string, customer_id: int, review_id: string, product_id: string, product_parent: int, product_title: string, product_category: string, star_rating: int, helpful_votes: int, total_votes: int, vine: string, verified_purchase: string, review_headline: string, review_body: string, review_date: string]"
            ]
          },
          "metadata": {},
          "execution_count": 8
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "totalvotes_df = df.filter(\"total_votes>=20\")\n",
        "totalvotes_df.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "3i8QilJDRc6l",
        "outputId": "8d3f01c6-3910-4a32-b089-a0f160bb4e46"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "+-----------+-----------+--------------+----------+--------------+--------------------+----------------+-----------+-------------+-----------+----+-----------------+--------------------+--------------------+-----------+\n",
            "|marketplace|customer_id|     review_id|product_id|product_parent|       product_title|product_category|star_rating|helpful_votes|total_votes|vine|verified_purchase|     review_headline|         review_body|review_date|\n",
            "+-----------+-----------+--------------+----------+--------------+--------------------+----------------+-----------+-------------+-----------+----+-----------------+--------------------+--------------------+-----------+\n",
            "|         US|   41681546| RL8D0KJ0J9L0O|B00BWC1X3S|     328960153|Zinus 14 Inch Eli...|       Furniture|          5|          152|        165|   N|                Y|A solid VICTORY f...|I've been looking...| 2015-08-31|\n",
            "|         US|   16806846|R1BEINAIQFBRJC|B007I81A60|      68465765|8\" Night Therapy ...|       Furniture|          5|           21|         23|   N|                Y|An Engineering Su...|A full size mattr...| 2015-08-31|\n",
            "|         US|   17820936|R2L59KIJH302P9|B007QULII0|     812343799|LexMod Stencil Di...|       Furniture|          4|           26|         26|   N|                Y|     Love this chair|Love this chair, ...| 2015-08-31|\n",
            "|         US|   50476494| RR99CPG695T0I|B013L4ZWWW|     124365349|Arctic Dreams 10\"...|       Furniture|          5|          215|        248|   N|                N| QUALITY* SLEEP!!!!!|I decided to get ...| 2015-08-31|\n",
            "|         US|   21846903|R1XQNKKUPCMWVO|B00IPN64CC|     867520220|Upholstered Platf...|       Furniture|          5|           43|         44|   N|                Y|Black Tufted Desi...|I have to admit t...| 2015-08-31|\n",
            "|         US|   36021042|R3JUXVCT1NSK2A|B003PSNAI8|     219454481|Fashion Bed Group...|       Furniture|          3|           25|         26|   N|                Y|Works but has odd...|Fully assembled i...| 2015-08-31|\n",
            "|         US|    2067832|R3GNSIFV1J2Y2B|B008RKOL9G|     589861187|Big Joe Media Lou...|       Furniture|          1|           15|         60|   N|                N|   Very disappointed|The chair itself ...| 2015-08-31|\n",
            "|         US|   15624624| RTCRZARYY4LXX|B00E97HPLW|     132456290|Flash Furniture M...|       Furniture|          5|           52|         54|   N|                Y|comfortable/easy ...|Everything I expe...| 2015-08-31|\n",
            "|         US|   13214979|R3OFB4P7Y8WR27|B00QBZ25R4|     637686095|Tuft & Needle Mat...|       Furniture|          1|           15|         26|   N|                Y|Most painful matt...|This product was ...| 2015-08-31|\n",
            "|         US|   37722720|R3MTAYGQM25N63|B007J0E7WQ|     562508640|Target Marketing ...|       Furniture|          4|           58|         59|   N|                Y|Good little cabin...|Purchased this on...| 2015-08-31|\n",
            "|         US|   31278317| RJNDSWES5ISZ7|B00HTUOOBA|     995797488|Chrome Metal Bar ...|       Furniture|          5|           78|         79|   N|                Y|             AMAZING|this is a very be...| 2015-08-31|\n",
            "|         US|   21515203|R15R7STOZZP2A4|B002V1Q65Y|     320882925|Coaster Company P...|       Furniture|          5|           33|         34|   N|                Y|         Great deal!|Good quality bed....| 2015-08-31|\n",
            "|         US|   48672213|R33V5WV529NK8E|B00MULXWMU|     491669252|Modway Annabel Tw...|       Furniture|          4|           30|         32|   N|                Y|           Worth it!|Great quality for...| 2015-08-31|\n",
            "|         US|   50914859| RIR9ZI3L80P7P|B00T3MUB4Q|      76857765|WinkBeds - Mattre...|       Furniture|          3|           72|         76|   N|                N|Disappointed - re...|**** UPDATED 02-2...| 2015-08-31|\n",
            "|         US|    7691605|R10P6SDC1D6C3I|B00LZM5IOK|     420170495|Modway Lily Twin ...|       Furniture|          5|           23|         25|   N|                Y|Like it! My bed i...|Like it ! My bed ...| 2015-08-31|\n",
            "|         US|   46509642|R110G9UVLI2MLS|B00OKIPS0A|     415535727|Milton Greens Sta...|       Furniture|          5|           52|         55|   N|                Y|             Lovely!|For those living ...| 2015-08-31|\n",
            "|         US|   47359106|R1I4LN1WR3YVJX|B00NUS5D4C|     148579574|AmazonBasics 5-Sh...|       Furniture|          1|           31|         40|   N|                Y|Cheap and frustra...|Cheap product, on...| 2015-08-31|\n",
            "|         US|   23511203|R1B76MPCS05UX9|B00P7RWWM0|     259554464|Mega Motion Easy ...|       Furniture|          5|           19|         21|   N|                Y|Great chair, Don'...|Ok this chair is ...| 2015-08-31|\n",
            "|         US|    6407891|R17PJIKAZ3U6BG|B00DW7LB0G|     366981061|Simpli Home Lared...|       Furniture|          5|           21|         21|   N|                Y|I love this beaut...|We love this benc...| 2015-08-30|\n",
            "|         US|    8113934|R2T3TLCX42RWLY|B009V5YVT6|     598492986|AVE SIX Reflectio...|       Furniture|          5|           46|         48|   N|                Y|      Beyond happy!!|Honestly, a pictu...| 2015-08-30|\n",
            "+-----------+-----------+--------------+----------+--------------+--------------------+----------------+-----------+-------------+-----------+----+-----------------+--------------------+--------------------+-----------+\n",
            "only showing top 20 rows\n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "helpful_50_df = totalvotes_df.filter(\"helpful_votes/total_votes>=.50\")\n",
        "helpful_50_df.show()\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "FeYwxibnRfsw",
        "outputId": "f2bc280c-e968-4706-8c10-e00570b2940b"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "+-----------+-----------+--------------+----------+--------------+--------------------+----------------+-----------+-------------+-----------+----+-----------------+--------------------+--------------------+-----------+\n",
            "|marketplace|customer_id|     review_id|product_id|product_parent|       product_title|product_category|star_rating|helpful_votes|total_votes|vine|verified_purchase|     review_headline|         review_body|review_date|\n",
            "+-----------+-----------+--------------+----------+--------------+--------------------+----------------+-----------+-------------+-----------+----+-----------------+--------------------+--------------------+-----------+\n",
            "|         US|   41681546| RL8D0KJ0J9L0O|B00BWC1X3S|     328960153|Zinus 14 Inch Eli...|       Furniture|          5|          152|        165|   N|                Y|A solid VICTORY f...|I've been looking...| 2015-08-31|\n",
            "|         US|   16806846|R1BEINAIQFBRJC|B007I81A60|      68465765|8\" Night Therapy ...|       Furniture|          5|           21|         23|   N|                Y|An Engineering Su...|A full size mattr...| 2015-08-31|\n",
            "|         US|   17820936|R2L59KIJH302P9|B007QULII0|     812343799|LexMod Stencil Di...|       Furniture|          4|           26|         26|   N|                Y|     Love this chair|Love this chair, ...| 2015-08-31|\n",
            "|         US|   50476494| RR99CPG695T0I|B013L4ZWWW|     124365349|Arctic Dreams 10\"...|       Furniture|          5|          215|        248|   N|                N| QUALITY* SLEEP!!!!!|I decided to get ...| 2015-08-31|\n",
            "|         US|   21846903|R1XQNKKUPCMWVO|B00IPN64CC|     867520220|Upholstered Platf...|       Furniture|          5|           43|         44|   N|                Y|Black Tufted Desi...|I have to admit t...| 2015-08-31|\n",
            "|         US|   36021042|R3JUXVCT1NSK2A|B003PSNAI8|     219454481|Fashion Bed Group...|       Furniture|          3|           25|         26|   N|                Y|Works but has odd...|Fully assembled i...| 2015-08-31|\n",
            "|         US|   15624624| RTCRZARYY4LXX|B00E97HPLW|     132456290|Flash Furniture M...|       Furniture|          5|           52|         54|   N|                Y|comfortable/easy ...|Everything I expe...| 2015-08-31|\n",
            "|         US|   13214979|R3OFB4P7Y8WR27|B00QBZ25R4|     637686095|Tuft & Needle Mat...|       Furniture|          1|           15|         26|   N|                Y|Most painful matt...|This product was ...| 2015-08-31|\n",
            "|         US|   37722720|R3MTAYGQM25N63|B007J0E7WQ|     562508640|Target Marketing ...|       Furniture|          4|           58|         59|   N|                Y|Good little cabin...|Purchased this on...| 2015-08-31|\n",
            "|         US|   31278317| RJNDSWES5ISZ7|B00HTUOOBA|     995797488|Chrome Metal Bar ...|       Furniture|          5|           78|         79|   N|                Y|             AMAZING|this is a very be...| 2015-08-31|\n",
            "|         US|   21515203|R15R7STOZZP2A4|B002V1Q65Y|     320882925|Coaster Company P...|       Furniture|          5|           33|         34|   N|                Y|         Great deal!|Good quality bed....| 2015-08-31|\n",
            "|         US|   48672213|R33V5WV529NK8E|B00MULXWMU|     491669252|Modway Annabel Tw...|       Furniture|          4|           30|         32|   N|                Y|           Worth it!|Great quality for...| 2015-08-31|\n",
            "|         US|   50914859| RIR9ZI3L80P7P|B00T3MUB4Q|      76857765|WinkBeds - Mattre...|       Furniture|          3|           72|         76|   N|                N|Disappointed - re...|**** UPDATED 02-2...| 2015-08-31|\n",
            "|         US|    7691605|R10P6SDC1D6C3I|B00LZM5IOK|     420170495|Modway Lily Twin ...|       Furniture|          5|           23|         25|   N|                Y|Like it! My bed i...|Like it ! My bed ...| 2015-08-31|\n",
            "|         US|   46509642|R110G9UVLI2MLS|B00OKIPS0A|     415535727|Milton Greens Sta...|       Furniture|          5|           52|         55|   N|                Y|             Lovely!|For those living ...| 2015-08-31|\n",
            "|         US|   47359106|R1I4LN1WR3YVJX|B00NUS5D4C|     148579574|AmazonBasics 5-Sh...|       Furniture|          1|           31|         40|   N|                Y|Cheap and frustra...|Cheap product, on...| 2015-08-31|\n",
            "|         US|   23511203|R1B76MPCS05UX9|B00P7RWWM0|     259554464|Mega Motion Easy ...|       Furniture|          5|           19|         21|   N|                Y|Great chair, Don'...|Ok this chair is ...| 2015-08-31|\n",
            "|         US|    6407891|R17PJIKAZ3U6BG|B00DW7LB0G|     366981061|Simpli Home Lared...|       Furniture|          5|           21|         21|   N|                Y|I love this beaut...|We love this benc...| 2015-08-30|\n",
            "|         US|    8113934|R2T3TLCX42RWLY|B009V5YVT6|     598492986|AVE SIX Reflectio...|       Furniture|          5|           46|         48|   N|                Y|      Beyond happy!!|Honestly, a pictu...| 2015-08-30|\n",
            "|         US|   48960668|R39YWJ09ZCPW7P|B00UXRSDF4|     949941628|2xhome - Black - ...|       Furniture|          5|           24|         28|   N|                Y|          Five Stars|Great chair great...| 2015-08-30|\n",
            "+-----------+-----------+--------------+----------+--------------+--------------------+----------------+-----------+-------------+-----------+----+-----------------+--------------------+--------------------+-----------+\n",
            "only showing top 20 rows\n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(helpful_50_df.count())"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "sNnpMkZWRhHU",
        "outputId": "3335945b-167e-4037-afec-d561b86d209b"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "18155\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "vine_review_df = helpful_50_df.filter(helpful_50_df[\"vine\"] == \"Y\")\n",
        "vine_review_df.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "NAam77k5Ri_Y",
        "outputId": "7f8473f1-a3bb-4dd5-da11-e70025159a6b"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "+-----------+-----------+--------------+----------+--------------+--------------------+----------------+-----------+-------------+-----------+----+-----------------+--------------------+--------------------+-----------+\n",
            "|marketplace|customer_id|     review_id|product_id|product_parent|       product_title|product_category|star_rating|helpful_votes|total_votes|vine|verified_purchase|     review_headline|         review_body|review_date|\n",
            "+-----------+-----------+--------------+----------+--------------+--------------------+----------------+-----------+-------------+-----------+----+-----------------+--------------------+--------------------+-----------+\n",
            "|         US|   35119071|R2BQOD1R0228FN|B00H2RSA88|     405483618|Sleep Innovations...|       Furniture|          3|           17|         26|   Y|                N|An okay product. ...|Three-stars is co...| 2015-08-27|\n",
            "|         US|   44737123| RC31RUPFOHBHQ|B0125QZ50G|     350975212|Zinus Viscolatex ...|       Furniture|          4|          102|        117|   Y|                N| Comfort and Support|I have not tried ...| 2015-08-24|\n",
            "|         US|   51369093| REN3N1WITLF1Y|B00S5EI4C4|     153136932|Brentwood Home S-...|       Furniture|          5|           33|         37|   Y|                N|       Pros and Cons|4.5 stars<br /><b...| 2015-08-20|\n",
            "|         US|   49598970| R71RZQ9UZVG47|B00H2RSA88|     405483618|Sleep Innovations...|       Furniture|          4|           38|         47|   Y|                N|Great memory foam...|This is a good me...| 2015-08-19|\n",
            "|         US|   50507621|R38NMQBH88HLM6|B00H2RSA88|     405483618|Sleep Innovations...|       Furniture|          4|           18|         24|   Y|                N|Firm......VERY fi...|Always wanted a m...| 2015-08-17|\n",
            "|         US|   44737123|R33FGX9EE3QVR6|B00K7G8M34|     291701473|Fashion Bed Group...|       Furniture|          4|           26|         26|   Y|                N|Solid, Smooth & Q...|This is our first...| 2015-08-08|\n",
            "|         US|   17957446|R1KIOIK6WEYE59|B00ZY8DOCY|     858354913|Harmony Ergonomic...|       Furniture|          3|           19|         20|   Y|                N|Great Idea, Disap...|When I saw this i...| 2015-07-19|\n",
            "|         US|   42483100|R25X9BMOB3FD0E|B00S5EI4C4|     153136932|Brentwood Home S-...|       Furniture|          4|           32|         37|   Y|                N|My 4th latex matt...|The liner is made...| 2015-07-19|\n",
            "|         US|   52464985|R3VCKFCX2377Q2|B00Y4BGT06|     383077572|Sleep Innovations...|       Furniture|          4|           95|        101|   Y|                N|A Nest For One or...|This is a two pie...| 2015-07-04|\n",
            "|         US|   46266548|R1E0OUG63HMSM4|B00Y4BGT06|     383077572|Sleep Innovations...|       Furniture|          3|           58|         61|   Y|                N|A thoughtful prod...|We're great fans ...| 2015-07-02|\n",
            "|         US|   51923814|R1V45RUW5ZB3LS|B00WO0S5EM|     720135802|Serta Pearce Firm...|       Furniture|          4|           19|         21|   Y|                N|Reluctant Memory ...|I was impressed w...| 2015-07-01|\n",
            "|         US|   52862683| RTF6DSZ1UTLHH|B00LJ7D280|     576833455|Classic Brands Gr...|       Furniture|          5|          401|        418|   Y|                N|So comfortable, a...|[[VIDEOID:2ff2135...| 2015-06-23|\n",
            "|         US|   51903105|R1CZV9N2YLJAP7|B00LJ7D280|     576833455|Classic Brands Gr...|       Furniture|          5|          123|        136|   Y|                Y|I am loving this ...|UPDATE: As I wrot...| 2015-06-21|\n",
            "|         US|   35575415|R1OF3X9W99Y300|B00LJ7D280|     576833455|Classic Brands Gr...|       Furniture|          4|           27|         35|   Y|                N|Soft-Med firmness...|[[VIDEOID:dcb995d...| 2015-06-20|\n",
            "|         US|   51956455|R1JYKEH4CQVJ1B|B00LJ7D280|     576833455|Classic Brands Gr...|       Furniture|          5|           22|         23|   Y|                N|Sorry for writing...|1) The Competitio...| 2015-06-18|\n",
            "|         US|   37982975|R1093XVB0H2QOL|B00Y4BGT06|     383077572|Sleep Innovations...|       Furniture|          4|           51|         54|   Y|                N|Sleeping on a clo...|I swear by foam m...| 2015-06-12|\n",
            "|         US|   22656237|R3Q81B31F1CPGH|B00P21TAIK|     298322939|Chill Sack Bean B...|       Furniture|          3|           50|         55|   Y|                N|             Massive|If there's only o...| 2015-06-02|\n",
            "|         US|   34160155|R2P6XIZZPJF7AE|B00P21TAIK|     298322939|Chill Sack Bean B...|       Furniture|          5|           46|         51|   Y|                N|Humans or cats ca...|Chill Bag is the ...| 2015-05-28|\n",
            "|         US|   33167968|R3N5S06UW5MKFE|B00UVAJUBO|     584650655|Classic Brands 10...|       Furniture|          3|          907|        925|   Y|                N|3 inches of real ...|If I have $400 to...| 2015-05-23|\n",
            "|         US|   52846213|R3J9EJCVKFCRWO|B00UA8TD6O|      78126929|Safavieh Tranquil...|       Furniture|          5|           18|         20|   Y|                N|Quality, Comfort ...|Whoever thought t...| 2015-05-20|\n",
            "+-----------+-----------+--------------+----------+--------------+--------------------+----------------+-----------+-------------+-----------+----+-----------------+--------------------+--------------------+-----------+\n",
            "only showing top 20 rows\n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "novine_review_df = helpful_50_df.filter(helpful_50_df[\"vine\"] == \"N\")\n",
        "novine_review_df.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "wFm83tixRkq8",
        "outputId": "1a5f393b-380e-43a0-d0c4-cd03d73bf19c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "+-----------+-----------+--------------+----------+--------------+--------------------+----------------+-----------+-------------+-----------+----+-----------------+--------------------+--------------------+-----------+\n",
            "|marketplace|customer_id|     review_id|product_id|product_parent|       product_title|product_category|star_rating|helpful_votes|total_votes|vine|verified_purchase|     review_headline|         review_body|review_date|\n",
            "+-----------+-----------+--------------+----------+--------------+--------------------+----------------+-----------+-------------+-----------+----+-----------------+--------------------+--------------------+-----------+\n",
            "|         US|   41681546| RL8D0KJ0J9L0O|B00BWC1X3S|     328960153|Zinus 14 Inch Eli...|       Furniture|          5|          152|        165|   N|                Y|A solid VICTORY f...|I've been looking...| 2015-08-31|\n",
            "|         US|   16806846|R1BEINAIQFBRJC|B007I81A60|      68465765|8\" Night Therapy ...|       Furniture|          5|           21|         23|   N|                Y|An Engineering Su...|A full size mattr...| 2015-08-31|\n",
            "|         US|   17820936|R2L59KIJH302P9|B007QULII0|     812343799|LexMod Stencil Di...|       Furniture|          4|           26|         26|   N|                Y|     Love this chair|Love this chair, ...| 2015-08-31|\n",
            "|         US|   50476494| RR99CPG695T0I|B013L4ZWWW|     124365349|Arctic Dreams 10\"...|       Furniture|          5|          215|        248|   N|                N| QUALITY* SLEEP!!!!!|I decided to get ...| 2015-08-31|\n",
            "|         US|   21846903|R1XQNKKUPCMWVO|B00IPN64CC|     867520220|Upholstered Platf...|       Furniture|          5|           43|         44|   N|                Y|Black Tufted Desi...|I have to admit t...| 2015-08-31|\n",
            "|         US|   36021042|R3JUXVCT1NSK2A|B003PSNAI8|     219454481|Fashion Bed Group...|       Furniture|          3|           25|         26|   N|                Y|Works but has odd...|Fully assembled i...| 2015-08-31|\n",
            "|         US|   15624624| RTCRZARYY4LXX|B00E97HPLW|     132456290|Flash Furniture M...|       Furniture|          5|           52|         54|   N|                Y|comfortable/easy ...|Everything I expe...| 2015-08-31|\n",
            "|         US|   13214979|R3OFB4P7Y8WR27|B00QBZ25R4|     637686095|Tuft & Needle Mat...|       Furniture|          1|           15|         26|   N|                Y|Most painful matt...|This product was ...| 2015-08-31|\n",
            "|         US|   37722720|R3MTAYGQM25N63|B007J0E7WQ|     562508640|Target Marketing ...|       Furniture|          4|           58|         59|   N|                Y|Good little cabin...|Purchased this on...| 2015-08-31|\n",
            "|         US|   31278317| RJNDSWES5ISZ7|B00HTUOOBA|     995797488|Chrome Metal Bar ...|       Furniture|          5|           78|         79|   N|                Y|             AMAZING|this is a very be...| 2015-08-31|\n",
            "|         US|   21515203|R15R7STOZZP2A4|B002V1Q65Y|     320882925|Coaster Company P...|       Furniture|          5|           33|         34|   N|                Y|         Great deal!|Good quality bed....| 2015-08-31|\n",
            "|         US|   48672213|R33V5WV529NK8E|B00MULXWMU|     491669252|Modway Annabel Tw...|       Furniture|          4|           30|         32|   N|                Y|           Worth it!|Great quality for...| 2015-08-31|\n",
            "|         US|   50914859| RIR9ZI3L80P7P|B00T3MUB4Q|      76857765|WinkBeds - Mattre...|       Furniture|          3|           72|         76|   N|                N|Disappointed - re...|**** UPDATED 02-2...| 2015-08-31|\n",
            "|         US|    7691605|R10P6SDC1D6C3I|B00LZM5IOK|     420170495|Modway Lily Twin ...|       Furniture|          5|           23|         25|   N|                Y|Like it! My bed i...|Like it ! My bed ...| 2015-08-31|\n",
            "|         US|   46509642|R110G9UVLI2MLS|B00OKIPS0A|     415535727|Milton Greens Sta...|       Furniture|          5|           52|         55|   N|                Y|             Lovely!|For those living ...| 2015-08-31|\n",
            "|         US|   47359106|R1I4LN1WR3YVJX|B00NUS5D4C|     148579574|AmazonBasics 5-Sh...|       Furniture|          1|           31|         40|   N|                Y|Cheap and frustra...|Cheap product, on...| 2015-08-31|\n",
            "|         US|   23511203|R1B76MPCS05UX9|B00P7RWWM0|     259554464|Mega Motion Easy ...|       Furniture|          5|           19|         21|   N|                Y|Great chair, Don'...|Ok this chair is ...| 2015-08-31|\n",
            "|         US|    6407891|R17PJIKAZ3U6BG|B00DW7LB0G|     366981061|Simpli Home Lared...|       Furniture|          5|           21|         21|   N|                Y|I love this beaut...|We love this benc...| 2015-08-30|\n",
            "|         US|    8113934|R2T3TLCX42RWLY|B009V5YVT6|     598492986|AVE SIX Reflectio...|       Furniture|          5|           46|         48|   N|                Y|      Beyond happy!!|Honestly, a pictu...| 2015-08-30|\n",
            "|         US|   48960668|R39YWJ09ZCPW7P|B00UXRSDF4|     949941628|2xhome - Black - ...|       Furniture|          5|           24|         28|   N|                Y|          Five Stars|Great chair great...| 2015-08-30|\n",
            "+-----------+-----------+--------------+----------+--------------+--------------------+----------------+-----------+-------------+-----------+----+-----------------+--------------------+--------------------+-----------+\n",
            "only showing top 20 rows\n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# BELOW IS ADDIITIONAL INFORMATION TO SUPPORT MY ANALYSIS"
      ],
      "metadata": {
        "id": "ZSihd2UbB2yX"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from pyspark.sql.functions import count\n",
        "# Total number of reviews for each dataframe from Step 3 and Step 4:\n",
        "vine_review_count = vine_review_df.count()\n",
        "print(\"Total Number of Reviews PAID and 'helpful': %f\" % vine_review_count)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "HC227vsrSVWm",
        "outputId": "093fc013-188a-44e0-d912-7cef6f76700e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Total Number of Reviews PAID and 'helpful': 136.000000\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "novine_review_count = novine_review_df.count()\n",
        "print(\"Total Number of Reviews NON-PAID and 'helpful': %f\" % novine_review_count)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "KZ92im2HTP1U",
        "outputId": "e4184ea3-0527-4c37-ff83-1461680dd2ae"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Total Number of Reviews NON-PAID and 'helpful': 18019.000000\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Percentage of 5-star Reviews for above Paid and Non-Paid dataframes\n",
        "star5_vine_pct = (star5_vine_df.count()/vine_review_count)\n",
        "print(\"Percent of 5-Star Furniture Reviews from PAID, 'helpful' dataset: %f\" % star5_vine_pct)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "0XFmVp6IT0Zt",
        "outputId": "1f11caab-15b2-4b8f-c646-721dee0eae55"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Percent of 5-Star Furniture Reviews from PAID, 'helpful' dataset: 0.544118\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "star5_novine_pct = (star5_novine_df.count()/novine_review_count)\n",
        "print(\"Percent of 5-Star Furniture Reviews from NON-PAID, 'helpful' dataset: %f\" % star5_novine_pct)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ivnM7bKjT37v",
        "outputId": "0442611e-ec56-4a8c-a798-0faef35820eb"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Percent of 5-Star Furniture Reviews from NON-PAID, 'helpful' dataset: 0.470725\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Total number of ALL reviews\n",
        "total_reviews_count = df.count()\n",
        "print(\"Total Number of Furniture Reviews: %f\" % total_reviews_count)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "WeELa8tsT6o7",
        "outputId": "c1539c4b-d861-46bd-c754-efb4693d88ab"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Total Number of Furniture Reviews: 792113.000000\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "star5_count = star5_df.count()\n",
        "print(\"Total Number of 5-Star Furniture Reviews: %f\" % star5_count)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "A8SzZqauUDve",
        "outputId": "77b72587-da53-4568-cae5-4aff707c97ec"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Total Number of 5-Star Furniture Reviews: 447716.000000\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Percentage of ALL 5-star reviews paid vs non-paid \n",
        "# 5-star Paid reviews \n",
        "vine_star5_all_df = star5_df.filter(star5_df[\"vine\"] == \"Y\")\n",
        "vine_star5_all_count = vine_star5_all_df.count()"
      ],
      "metadata": {
        "id": "r6MKKb3zUN5N"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "vine_star5_all_pct = (vine_star5_all_count/star5_count)\n",
        "print(\"Number of 5-Star Furniture Reviews PAID: %f\" % vine_star5_all_count)\n",
        "print(\"Percent of 5-Star Furniture Reviews PAID: %f\" % vine_star5_all_pct)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "vxMN2F_TUSkr",
        "outputId": "ab80b19a-e624-4abb-ab1a-cf576b54ea55"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Number of 5-Star Furniture Reviews PAID: 1356.000000\n",
            "Percent of 5-Star Furniture Reviews PAID: 0.003029\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        " \n",
        "#5-star Non-Paid reviews\n",
        "novine_star5_all_df = star5_df.filter(star5_df[\"vine\"] == \"N\")\n",
        "novine_star5_all_count = novine_star5_all_df.count()"
      ],
      "metadata": {
        "id": "L789u8FRUUlV"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "novine_star5_all_pct = novine_star5_all_count/star5_count\n",
        "print(\"Number of 5-Star Furniture Reviews NON-PAID: %f\" % novine_star5_all_count)\n",
        "print(\"Percent of 5-Star Furniture Reviews NON-PAID: %f\" % novine_star5_all_pct)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "kAKQRKITUXUW",
        "outputId": "c6d01e5f-0c96-4cd5-c455-572cef6626e3"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Number of 5-Star Furniture Reviews NON-PAID: 446360.000000\n",
            "Percent of 5-Star Furniture Reviews NON-PAID: 0.996971\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Percent of Vine vs non-Vine all reviews\n",
        "vine_all_df = df.filter(df[\"vine\"] == \"Y\")\n",
        "novine_all_df = df.filter(df[\"vine\"] == \"N\")\n",
        "vine_pct_all = (vine_all_df.count()/df.count())\n",
        "novine_pct_all = (novine_all_df.count()/df.count())\n",
        "print(vine_pct_all)\n",
        "print(novine_pct_all)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "p19M2fHbUrfv",
        "outputId": "c578082c-1d39-4109-87cb-df38983cd0b9"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "0.003503288040973952\n",
            "0.996496711959026\n"
          ]
        }
      ]
    }
  ]
}