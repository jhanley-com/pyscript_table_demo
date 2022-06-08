try:
	from error_handler import errorHandler
	import asyncio
	from pyodide import create_proxy
	from jhanley_html import HTML
except Exception as e:
	errorHandler(e)

def build_table(contacts):
	header_row = [
		'First Name',
		'Last Name',
		'Phone Number'
	]

	table_data = []

	for item in contacts:
		entry = []
		for k in item:
			console.log('ITEM: {}: {}'.format(k, item[k]))
			entry.append(item[k])

		table_data.append(entry)

	HTML().table(header_row=header_row, table_data=table_data)

async def main():
	try:
		contacts = [
			{
				'firstname': 'John',
				'lastname': 'Smith',
				'telephone': '123-456-7890'
			},
			{
				'firstname': 'Sally',
				'lastname': 'Rogers',
				'telephone': '345-425-7100'
			},
			{
				'firstname': 'Buck',
				'lastname': 'Ford',
				'telephone': '882-885-4501'
			},
		]

		build_table(contacts)
	except Exception as e:
		errorHandler(e)

main()
