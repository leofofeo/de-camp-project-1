ticker_data = """
AMD
	Advanced Micro Devices, Inc.	160.43	-5.09	-3.08%	90.631M	60.814M	267.533B	232.51	
NVDA
	NVIDIA Corporation	1,037.99	+88.49	+9.32%	83.071M	49.054M	2.553T	60.59	
NIO
	NIO Inc.	4.8000	-0.4400	-8.40%	78.373M	57.346M	10.684B	N/A	
TSLA
	Tesla, Inc.	173.74	-6.37	-3.54%	71.092M	97.245M	574.405B	44.43	
SOFI
	SoFi Technologies, Inc.	6.83	-0.19	-2.71%	53.73M	49.447M	7.422B	N/A	
INTC
	Intel Corporation	30.08	-1.34	-4.26%	61.73M	49.516M	133.751B	31.01	
F
	Ford Motor Company	12.11	+0.08	+0.67%	41.274M	48.964M	47.803B	12.48	
MARA
	Marathon Digital Holdings, Inc.	20.08	-1.16	-5.46%	42.564M	57.636M	5.481B	12.55	
AAPL
	Apple Inc.	186.88	-4.02	-2.11%	50.482M	63.953M	2.927T	29.06	
PFE
	Pfizer Inc.	28.69	-0.91	-3.07%	41.883M	42.678M	167.731B	N/A	
ETRN
	Equitrans Midstream Corporation	13.84	0.00	0.00%	36.241M	7.691M	6.002B	15.38	
RIVN
	Rivian Automotive, Inc.	9.95	-0.75	-7.01%	37.08M	44.255M	10.65B	N/A	
PLTR
	Palantir Technologies Inc.	20.72	-0.45	-2.13%	36.476M	50.788M	46.141B	172.67	
SIRI
	Sirius XM Holdings Inc.	2.7300	-0.0700	-2.50%	33.762M	18.46M	10.501B	8.27	
BAC
	Bank of America Corporation	39.17	-0.59	-1.48%	38.561M	38.377M	310.938B	13.51	
CLSK
	CleanSpark, Inc.	17.09	-1.35	-7.32%	32.064M	35.489M	3.894B	131.46	
WBD
	Warner Bros. Discovery, Inc.	7.70	-0.36	-4.47%	35.692M	30.725M	19.749B	N/A	
GME
	GameStop Corp.	18.32	-2.80	-13.26%	29.792M	20.566M	5.609B	916.00	
CCL
	Carnival Corporation & plc	14.78	-0.87	-5.56%	31.935M	30.653M	19.362B	46.19	
AAL
	American Airlines Group Inc.	13.82	-0.28	-1.99%	29.062M	29.931M	9.251B	19.46	
AMZN
	Amazon.com, Inc.	181.05	-2.08	-1.14%	32.901M	39.543M	1.906T	50.71	
PLUG
	Plug Power Inc.	3.0750	-0.3350	-9.82%	28.071M	35.842M	2.532B	N/A	
VFC
	V.F. Corporation	11.97	-0.36	-2.92%	27.036M	9.301M	4.655B	N/A	
T
	AT&T Inc.	17.47	-0.03	-0.17%	32.151M	35.158M	125.263B	9.39	
MPW
	Medical Properties Trust, Inc.	5.04	+0.09	+1.82%	25.437M	20.238M	3.026B	N/A	
GRAB
	Grab Holdings Limited	3.6700	-0.0300	-0.81%	24.294M	25.752M	14.626B	N/A	
GOLD
	Barrick Gold Corporation	16.94	-0.35	-2.02%	23.526M	23.625M	30.45B	20.66	
VALE
	Vale S.A.	12.58	-0.07	-0.55%	20.966M	27.304M	55.293B	6.95	
BABA
	Alibaba Group Holding Limited	80.80	-1.88	-2.27%	23.361M	16.175M	207.045B	18.36	
PDD
	PDD Holdings Inc.	153.63	+6.54	+4.45%	21.33M	9.724M	213.357B	20.00	
KGC
	Kinross Gold Corporation	7.88	-0.05	-0.63%	20.316M	16.684M	9.757B	21.89	
XPEV
	XPeng Inc.	8.10	-0.65	-7.43%	21.145M	15.832M	7.93B	N/A	
LCID
	Lucid Group, Inc.	2.7200	-0.1700	-5.88%	20.434M	26.603M	6.275B	N/A	
ERIC
	Telefonaktiebolaget LM Ericsson (publ)	5.87	-0.08	-1.34%	19.467M	16.808M	19.559B	N/A	
TSM
	Taiwan Semiconductor Manufacturing Company Limited	157.09	+0.94	+0.60%	20.832M	15.298M	814.783B	30.21	
JD
	JD.com, Inc.	31.20	-1.48	-4.53%	19.702M	14.855M	48.51B	13.99	
YMM
	Full Truck Alliance Co. Ltd.	8.93	-0.30	-3.25%	18.771M	9.112M	9.339B	31.89	
CSCO
	Cisco Systems, Inc.	46.60	-0.83	-1.75%	18.813M	19.08M	187.743B	15.74	
SNOW
	Snowflake Inc.	154.58	-8.76	-5.36%	19.381M	6.725M	54.588B	N/A	
UBER
	Uber Technologies, Inc.	63.60	-1.88	-2.87%	20.08M	18.324M	132.893B	100.95	
MU
	Micron Technology, Inc.	126.27	-0.01	-0.01%	20.246M	23.065M	139.839B	N/A	
NVAX
	Novavax, Inc.	15.15	-0.55	-3.50%	17.671M	12.952M	2.313B	N/A	
ABEV
	Ambev S.A.	2.2800	-0.0200	-0.87%	17.46M	14.699M	36.787B	12.67	
RIOT
	Riot Platforms, Inc.	9.97	-0.82	-7.60%	17.715M	24.471M	3.116B	23.74	
FCX
	Freeport-McMoRan Inc.	51.20	-0.03	-0.06%	16.851M	15.683M	73.591B	44.91	
DELL
	Dell Technologies Inc.	153.57	+5.79	+3.92%	16.211M	8.989M	109.105B	35.22	
EQT
	EQT Corporation	39.91	-1.30	-3.15%	16.232M	6.967M	17.624B	29.56	
ET
	Energy Transfer LP	15.41	-0.32	-2.03%	16.726M	11.136M	51.932B	14.14	
BEKE
	KE Holdings Inc.	16.99	-1.88	-9.96%	16.671M	9.625M	23.284B	24.62	
NU
	Nu Holdings Ltd.	11.57	-0.13	-1.11%	17.018M	24.495M	55.317B	44.50	
XOM
	Exxon Mobil Corporation	113.51	-1.97	-1.71%	15.711M	17.998M	518.035B	13.91	
DKNG
	DraftKings Inc.	40.60	-1.30	-3.10%	16.549M	9.97M	19.64B	N/A	
BA
	The Boeing Company	172.21	-14.07	-7.55%	16.69M	7.816M	105.717B	N/A	
PBR
	Petróleo Brasileiro S.A. - Petrobras	14.89	-0.11	-0.73%	15.678M	23.059M	96.11B	4.33	
HOOD
	Robinhood Markets, Inc.	19.24	-0.42	-2.14%	16.977M	16.874M	17.278B	137.43	
HPE
	Hewlett Packard Enterprise Company	18.24	+0.09	+0.50%	15.258M	15.433M	23.709B	12.58	
XP
	XP Inc.	18.47	+0.48	+2.67%	15.58M	5.778M	9.866B	12.56	
CVS
	CVS Health Corporation	55.65	-1.79	-3.12%	18.244M	11.457M	69.861B	9.76	
CYTK
	Cytokinetics, Incorporated	48.98	-10.25	-17.31%	15.398M	2.135M	5.136B	N/A	
GOOGL
	Alphabet Inc.	173.55	-2.83	-1.60%	20.549M	30.469M	2.189T	26.58	
BBD
	Banco Bradesco S.A.	2.5100	-0.0300	-1.18%	15.161M	16.038M	26.655B	10.91	
SNAP
	Snap Inc.	15.18	-0.73	-4.59%	15.868M	28.863M	26.109B	N/A	
SCHW
	The Charles Schwab Corporation	72.34	-2.93	-3.89%	14.55M	7.379M	132.25B	30.27	
WBA
	Walgreens Boots Alliance, Inc.	15.95	-0.52	-3.16%	15.913M	11.345M	13.76B	N/A	
BE
	Bloom Energy Corporation	15.73	-1.27	-7.47%	15.8M	6.349M	3.571B	N/A	
BILI
	Bilibili Inc.	13.74	-1.94	-12.37%	14.335M	8.046M	6.473B	N/A	
NCLH
	Norwegian Cruise Line Holdings Ltd.	15.57	-0.69	-4.24%	15.127M	14.215M	6.68B	19.22	
VZ
	Verizon Communications Inc.	39.43	-0.36	-0.90%	14.029M	17.887M	167.476B	14.77	
KVUE
	Kenvue Inc.	19.44	-0.44	-2.21%	15.116M	19.903M	37.224B	24.92	
BCS
	Barclays PLC	10.91	+0.07	+0.65%	13.655M	16.346M	41.316B	8.27	
LI
	Li Auto Inc.	19.58	-1.19	-5.73%	13.373M	9.69M	20.913B	12.97	
DNN
	Denison Mines Corp.	2.2400	0.0000	0.00%	12.654M	16.202M	2.015B	37.33	
MSFT
	Microsoft Corporation	427.00	-3.52	-0.82%	17.167M	19.644M	3.2T	37.03	
UAA
	Under Armour, Inc.	6.72	-0.23	-3.31%	12.481M	7.582M	2.885B	7.55	
GOOG
	Alphabet Inc.	175.06	-2.94	-1.65%	14.904M	22.522M	2.189T	26.89	
SBUX
	Starbucks Corporation	78.31	-2.42	-2.99%	15.816M	10.88M	91.431B	21.57	
MRVL
	Marvell Technology, Inc.	75.02	+1.34	+1.82%	15.474M	13.346M	64.928B	N/A	
PARA
	Paramount Global	11.79	-0.41	-3.36%	12.014M	21.29M	8.529B	N/A	
NOK
	Nokia Oyj	3.8500	-0.1000	-2.53%	11.967M	14.831M	21.831B	24.06	
KMI
	Kinder Morgan, Inc.	19.08	-0.31	-1.60%	11.433M	13.065M	42.346B	17.50	
WMT
	Walmart Inc.	64.84	-0.41	-0.63%	16.13M	16.863M	525.902B	27.83	
LYFT
	Lyft, Inc.	15.43	-0.68	-4.22%	12.428M	13.947M	6.226B	N/A	
CMCSA
	Comcast Corporation	38.68	-0.21	-0.54%	14.017M	20.928M	151.766B	10.26	
GFS
	GLOBALFOUNDRIES Inc.	50.49	-4.72	-8.55%	12.15M	1.52M	30.668B	31.36	
LUV
	Southwest Airlines Co.	26.65	-1.23	-4.41%	11.109M	9.23M	15.949B	41.64	
IP
	International Paper Company	44.16	+2.52	+6.06%	12.327M	6.658M	15.338B	83.32	
SMCI
	Super Micro Computer, Inc.	847.38	-25.89	-2.96%	11.345M	7.23M	49.62B	47.18	
NYCB
	New York Community Bancorp, Inc.	3.2300	-0.0900	-2.71%	11.045M	30.347M	2.651B	N/A	
KEY
	KeyCorp	14.46	-0.57	-3.79%	12.622M	12.862M	13.634B	18.54	
DD
	DuPont de Nemours, Inc.	78.93	+0.38	+0.48%	11.002M	2.425M	33.001B	85.79	
ITUB
	Itaú Unibanco Holding S.A.	6.24	-0.04	-0.64%	10.927M	16.035M	61.165B	9.45	
U
	Unity Software Inc.	19.60	-0.85	-4.16%	11.754M	9.261M	7.661B	N/A	
QCOM
	QUALCOMM Incorporated	201.76	-1.17	-0.58%	13.395M	8.273M	225.164B	26.87	
HBAN
	Huntington Bancshares Incorporated	13.58	-0.34	-2.44%	11.733M	15.577M	19.681B	12.23	
BMY
	Bristol-Myers Squibb Company	41.54	-0.80	-1.89%	12.364M	15.504M	85.827B	N/A	
SHOP
	Shopify Inc.	57.64	-1.06	-1.81%	10.915M	9.638M	74.264B	N/A	
RUN
	Sunrun Inc.	11.99	-0.93	-7.20%	11.227M	12.925M	2.658B	N/A	
VRT
	Vertiv Holdings Co	101.24	+1.11	+1.11%	10.652M	8.564M	37.899B	96.42	
WFC
	Wells Fargo & Company	59.68	-1.25	-2.05%	12.908M	18.313M	212.421B	12.43	
HIMS
"""
TICKERS = [line.split()[0] for line in ticker_data.split("\n") if line]
TICKERS = [ticker for ticker in TICKERS if len(ticker) >=1 and len(ticker) < 6 and ticker.isupper() and ticker.isalpha()]
TICKERS = set(TICKERS)
