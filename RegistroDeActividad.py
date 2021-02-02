import hashlib
import mysql.connector
import datetime
from time import ctime
import ntplib
from time import clock

x = 0
while True:
    y = clock()
    if y - x > 60:
		caracteres = "abcdefghijklmnopqrstuvwxyz0123456789"

		def generar_cadena():
			cadena = ""
			for ciclo in range(1,10):
				cadena = cadena + random.choice(caracteres)
			return cadena

		cadena = generar_cadena()
		firma_md5 = (hashlib.md5(cadena.encode())).hexdigest()
		firma_sha1 = (hashlib.sha1(cadena.encode())).hexdigest()
		firma_sha224 = (hashlib.sha224(cadena.encode())).hexdigest()
		firma_sha256 = (hashlib.sha256(cadena.encode())).hexdigest()
		firma_sha384 = (hashlib.sha384(cadena.encode())).hexdigest()
		firma_sha512 = (hashlib.sha512(cadena.encode())).hexdigest()

		servidor_de_tiempo = "time-e-g.nist.gov"
		cliente_ntp = ntplib.NTPClient()
		respuesta = cliente_ntp.request(servidor_de_tiempo)
		hora_actual = datetime.datetime.strptime(ctime(respuesta.tx_time), "%a %b %d %H:%M:%S %Y")
		a = str(hora_actual)
		z = a.split()
		fecha = z[0]
		hora = z[1]
		latitud = 19.698953
		longitud = -101.245623

		miConexion = mysql.connector.connect( host='localhost', user= 'alexis', passwd='12345', db='proyectoiot' )
		cur = miConexion.cursor()
		sql= "INSERT INTO registro(firma, latitud, longitud, fecha, hora) VALUES(%s, %s, %s, %s, %s)"
		datos = (firma_md5 , latitud, longitud, fecha, hora)
		cur.execute(sql, datos)
		miConexion.commit()
		miConexion.close()
		print("Dato capturado")
		x = y