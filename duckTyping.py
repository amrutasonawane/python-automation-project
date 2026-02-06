#Duck typing : it is a concept where the type of an object is determind by its behaviour not by its class 
class InkjetPrinter:
	def printDocument(self,document):
		print("InkjetPrinter printing : ", document)

class LaserPrinter:
	def printDocument(self,document):
		print("LaserPrinter printing : ", document)

class PDFWriter:
	def printDocument(self,document):
		print(f"Saving {document} as PDF")

def startPrinting(Device):
	Device.printDocument("marvellous notes")

def main():
	startPrinting(InkjetPrinter())
	startPrinting(LaserPrinter())
	startPrinting(PDFWriter())


main()
