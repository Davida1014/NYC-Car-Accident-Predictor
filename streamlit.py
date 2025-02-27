import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

st.title('NYC Car Accident Predictor')

@st.cache
def load_data():
	# Load data
	bkln = pd.read_csv('./Data/data_preds_bkln.csv')
	qns = pd.read_csv('./Data/data_preds_qns.csv')
	man = pd.read_csv('./Data/data_preds_man.csv')
	bx = pd.read_csv('./Data/data_preds_bx.csv')
	si = pd.read_csv('./Data/data_preds_si.csv')


	# Clean data
	# Set date column to datetime object
	bkln['Date'] = pd.to_datetime(bkln['Unnamed: 0'])
	bkln.drop(columns='Unnamed: 0', inplace=True)

	qns['Date'] = pd.to_datetime(qns['Unnamed: 0'])
	qns.drop(columns='Unnamed: 0', inplace=True)

	man['Date'] = pd.to_datetime(man['Unnamed: 0'])
	man.drop(columns='Unnamed: 0', inplace=True)

	bx['Date'] = pd.to_datetime(bx['Date'])

	si['Date'] = pd.to_datetime(si['Date'])


	bkln.set_index('Date', inplace=True)

	qns.set_index('Date', inplace=True)

	man.set_index('Date', inplace=True)

	bx.set_index('Date', inplace=True)
	
	si.set_index('Date', inplace=True)



	# Rename accidents column
	bkln.rename(columns={'0': 'Accidents'}, inplace=True)

	qns.rename(columns={'0': 'Accidents'}, inplace=True)

	man.rename(columns={'0': 'Accidents'}, inplace=True)

	bx.rename(columns={'0': 'Accidents'}, inplace=True)

	si.rename(columns={'0': 'Accidents'}, inplace=True)


	# Convert accidents to integers
	bkln['Accidents'] = bkln['Accidents'].astype(int)

	qns['Accidents'] = qns['Accidents'].astype(int)

	man['Accidents'] = man['Accidents'].astype(int)
	
	bx['Accidents'] = bx['Accidents'].astype(int)

	si['Accidents'] = si['Accidents'].astype(int)



	return bkln, qns, man, bx, si

@st.cache
def load_latlong():
	# Load data
	df_latlong = pd.read_csv('./Data/df_latlong.csv')


	# Convert date to datetime object
	df_latlong['Date'] = pd.to_datetime(df_latlong['Date'])

	# Change lat/lon column names
	df_latlong.rename(columns={'LATITUDE': 'lat', 'LONGITUDE': 'lon'}, inplace=True)

	return df_latlong


bkln, qns, man, bx, si = load_data()
df_latlong = load_latlong()

st.image('./Images/traffic.jpg')

st.write('Known data through January 29, 2021, predicted data through June 30, 2022.')


if st.checkbox('View All Historical Data'):
	with st.spinner('Loading data...'):
		dates = pd.date_range(start='2012-07-01', end='2021-01-29')
		date = st.selectbox('Select Date', dates, 0)

		st.map(df_latlong[df_latlong['Date']==date])

if st.checkbox('View By Borough and Date'):
	# Borough selection
	borough = st.selectbox('Select Borough',['The Bronx','Brooklyn','Manhattan', 'Queens','Staten Island','All'],5)

	# Date selection
	# Define date range
	dates = pd.date_range(start='2012-07-01', end='2022-07-01')
	date = st.selectbox('Select Date', dates, 0)
	st.write('Note: Data through 2021-01-29 is historical. Later accident counts are 	predictions.') 

	# Output
	if borough == 'The Bronx':
		st.subheader('Bronx Data')
		if date <= pd.to_datetime('2020-1-29'):
			st.write('The number of car accidents in The Bronx on this date was: ', bx['Accidents'][date])
		if date > pd.to_datetime('2020-1-29'):
			st.write('The number of car accidents in The Bronx on this date is 	predicted to be: ', bx['Accidents'][date])
		st.line_chart(bx)

	if borough == 'Brooklyn':
		st.subheader('Brooklyn Data')
		if date <= pd.to_datetime('2020-1-29'):
			st.write('The number of car accidents in Brooklyn on this date was: ', bkln['Accidents'][date])
		if date > pd.to_datetime('2020-1-29'):
			st.write('The number of car accidents in Brooklyn on this date is 	predicted to be: ', bkln['Accidents'][date])
		st.line_chart(bkln)

	if borough == 'Manhattan':
		st.subheader('Manhattan Data')
		if date <= pd.to_datetime('2020-1-29'):
			st.write('The number of car accidents in Manhattan on this date was: ', man['Accidents'][date])
		if date > pd.to_datetime('2020-1-29'):
			st.write('The number of car accidents in Manhattan on this date is 	predicted to be: ', man['Accidents'][date])
		st.line_chart(man)

	if borough == 'Queens':
		st.subheader('Queens Data')
		if date <= pd.to_datetime('2020-1-29'):
			st.write('The number of car accidents in Queens on this date was: ', qns['Accidents'][date])
		if date > pd.to_datetime('2020-1-29'):
			st.write('The number of car accidents in Queens on this date is predicted to be: ', qns['Accidents'][date])
		st.line_chart(qns)

	if borough == 'Staten Island':
		st.subheader('Staten Island Data')
		if date <= pd.to_datetime('2020-1-29'):
			st.write('The number of car accidents in Staten Island on this date was: ', si['Accidents'][date])
		if date > pd.to_datetime('2020-1-29'):
			st.write('The number of car accidents in Staten Island on this date is 	predicted to be: ', si['Accidents'][date])
		st.line_chart(si)

	if borough == 'All':

		st.subheader('Bronx Data')
		if date <= pd.to_datetime('2020-1-29'):
			st.write('The number of car accidents in The Bronx on this date was: ', bx['Accidents'][date])
		if date > pd.to_datetime('2020-1-29'):
			st.write('The number of car accidents in The Bronx on this date is 	predicted to be: ', bx['Accidents'][date])
		st.line_chart(bx)

		st.subheader('Brooklyn Data')
		if date <= pd.to_datetime('2020-1-29'):
			st.write('The number of car accidents in Brooklyn on this date was: ', bkln['Accidents'][date])
		if date > pd.to_datetime('2020-1-29'):
			st.write('The number of car accidents in Brooklyn on this date is predicted to be: ', bkln['Accidents'][date])
		st.line_chart(bkln)

		st.subheader('Manhattan Data')
		if date <= pd.to_datetime('2020-1-29'):
			st.write('The number of car accidents in Manhattan on this date was: ', man['Accidents'][date])
		if date > pd.to_datetime('2020-1-29'):
			st.write('The number of car accidents in Manhattan on this date is 	predicted to be: ', man['Accidents'][date])
		st.line_chart(man)

		st.subheader('Queens Data')
		if date <= pd.to_datetime('2020-1-29'):
			st.write('The number of car accidents in Queens on this date was: ', qns['Accidents'][date])
		if date > pd.to_datetime('2020-1-29'):
			st.write('The number of car accidents in Queens on this date is predicted to be: ', qns['Accidents'][date])
		st.line_chart(qns)

		st.subheader('Staten Island Data')
		if date <= pd.to_datetime('2020-1-29'):
			st.write('The number of car accidents in Staten Island on this date was: ', si['Accidents'][date])
		if date > pd.to_datetime('2020-1-29'):
			st.write('The number of car accidents in Staten Island on this date is 	predicted to be: ', si['Accidents'][date])
		st.line_chart(si)




st. write('For more information about this project, please visit its GitHub repository: https://github.com/Davida1014/NYC-Car-Accident-Predictor')



