import hashlib
class passwdops():
	def encrypt256(passwd):
		encryptstr=hashlib.sha256(passwd.encode()).hexdigest()
		return encryptstr
	