# coinbase-report
This program will use your Coinbase transaction history to generate a basic tax report based on the current price of the asset.

## Prerequisites

This program uses **python3** and **pip3** to install the dependencies.

## Cloning this repository

Assuming that you already have git installed on your computer, run the below command to clone this repository.

```bash
git clone https://github.com/tyleratracey/coinbase-report.git
```
## Installing dependencies

Once you have the repo cloned, use pip3 to install the dependencies from the requirements.txt file.

```bash
cd coinbase-report/
pip3 install -r requirements.txt
```

## Getting your Coinbase transaction history CSV file

In order to download your transaction history from Coinbase, log into your account and click on the profile icon in the top right hand corner, then select **Taxes and Reports**.

Scroll down to the **Transaction History** section and select **Generate Report**.

Download the CSV report.

## Running the program

Copy and paste the CSV file you just downloaded into the coinbase-history.csv file.

Open up the config.json file and add the assets you would like to run a report on as a comma separated list **("BTC","ETH","ADA")**, and set the value of your tax percentage. You can find out your tax bracket information online. Normally in the US, long term capital gains tax is around 15% **(0.15)**.

Once you have those files saved, run the report!

```bash
python3 run.py
```

## Donations

If you found this program useful, please consider donating!

```
BTC Address: 
ETH Address: 0xA71D242C222DADe9810f231465189a7b8669e154
ADA Address: 
```



