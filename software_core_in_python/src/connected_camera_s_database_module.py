import sqlite3

def verification_of_datas_existence_function(sough_field, concerned_table, concerned_field, concerned_data):

	results_number = None

	try:

		connected_camera_s_database_connexion = sqlite3.connect('src/connected_camera_s_database.db')

		connexion_s_cursor = connected_camera_s_database_connexion.cursor()

		#sql_query_string = "SELECT COUNT(" + sough_field + ") FROM " + concerned_table + " WHERE " + concerned_field + " = " + concerned_data + ""
		sql_query_string = "SELECT COUNT({}) FROM {} WHERE {} = {}".format(sough_field, concerned_table, concerned_field, concerned_data)

		connexion_s_cursor.execute(sql_query_string)

		results_number = connexion_s_cursor.fetchone()

		connexion_s_cursor.close()

	except sqlite3.Error as SQLError:

		print("SQL Error: ", SQLError)

	finally:

		if(connected_camera_s_database_connexion):

			connected_camera_s_database_connexion.close()

		return results_number
