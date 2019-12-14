import sqlite3

def selection_of_desired_fourcc_function(desired_format):

	desired_fourcc = None

	try:

		connected_camera_s_database_connexion = sqlite3.connect('src/connected_camera_s_database.db')

		connexion_s_cursor = connected_camera_s_database_connexion.cursor()

		sql_query_string = "SELECT associated_fourcc FROM supported_video_formats_table WHERE video_format_extension = '{}'".format(desired_format)

		connexion_s_cursor.execute(sql_query_string)

		sql_query_result = connexion_s_cursor.fetchone()

		desired_fourcc = sql_query_result[0]

		connexion_s_cursor.close()

	except sqlite3.Error as SQLError:

		print("SQL Error: ", SQLError)

	finally:

		if(connected_camera_s_database_connexion):

			connected_camera_s_database_connexion.close()

		return desired_fourcc

def verification_of_datas_existence_function(sough_field, concerned_table, concerned_field, concerned_data):

	data_exists = False

	try:

		connected_camera_s_database_connexion = sqlite3.connect('src/connected_camera_s_database.db')

		connexion_s_cursor = connected_camera_s_database_connexion.cursor()

		sql_query_string = "SELECT COUNT({}) FROM {} WHERE {} = {}".format(sough_field, concerned_table, concerned_field, concerned_data)

		connexion_s_cursor.execute(sql_query_string)

		results_number = connexion_s_cursor.fetchone()

		data_exists = bool(results_number[0])

		connexion_s_cursor.close()

	except sqlite3.Error as SQLError:

		print("SQL Error: ", SQLError)

	finally:

		if(connected_camera_s_database_connexion):

			connected_camera_s_database_connexion.close()

		return data_exists
