# coinbase-report
**This program will use your Coinbase transaction history to generate a basic tax report based on the current price of the asset.**

![alt text](https://github.com/tyleratracey/coinbase-report/blob/main/png/example_run.png?raw=true)

## Prerequisites

- This program uses **python3** and **pip3** to install the dependencies.

## Cloning this repository

- Assuming that you already have git installed on your computer, run the below command to clone this repository.

```bash
git clone https://github.com/tyleratracey/coinbase-report.git
```
## Installing dependencies

- Once you have the repo cloned, use pip3 to install the dependencies from the requirements.txt file.

```bash
cd coinbase-report/
pip3 install -r requirements.txt
```

## Getting your Coinbase transaction history CSV file

- In order to download your transaction history from Coinbase, log into your account and click on the profile icon in the top right hand corner, then select **Taxes and Reports**.

![alt text](https://github.com/tyleratracey/coinbase-report/blob/main/png/profile.png?raw=true)

- Scroll down to the **Transaction History** section and select **Generate Report**.

![alt text](https://github.com/tyleratracey/coinbase-report/blob/main/png/transaction_history.png?raw=true)

- Download the CSV report.

![alt text](https://github.com/tyleratracey/coinbase-report/blob/main/png/generate_report.png?raw=true)

## Running the program

- Copy and paste the CSV file you just downloaded into the coinbase-history.csv file, **and remove the first 7 lines so you are left with just the headers and data.**

![alt text](https://github.com/tyleratracey/coinbase-report/blob/main/png/csv.png?raw=true)

- Open up the **config.json** file and add the assets you would like to run a report on as a comma separated list **Example: "BTC,ETH,ADA"**, and set the value of your tax percentage. You can find out your tax bracket information online. Normally in the US, long term capital gains tax is around 15% **Example: "0.15"**.

![alt text](https://github.com/tyleratracey/coinbase-report/blob/main/png/config.png?raw=true)

- Once you have those files saved, run the report!

```bash
python3 run.py
```

![alt text](https://github.com/tyleratracey/coinbase-report/blob/main/png/results.png?raw=true)

## Donations

**If you found this program useful, please consider donating!**

```
BTC Address: 3CgpTmhi8NCcYZmFQU7m2MLkqDjQNoGHSG
ETH Address: 0xA71D242C222DADe9810f231465189a7b8669e154
ADA Address: addr1qylrz6cal0k9lu9p3jang2runtv8zd3v9wmu0jd0xaa7edqmjx2srq8kpxjuy2ewfun02hzdysyga6qx2phqa4e9v9msdvvde7
```



