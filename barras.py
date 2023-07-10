from asposebarcode import Recognition, Assist
# Setting License to read Barcode
licenseReadBarCode = Assist.License()
licenseReadBarCode.setLicense("Aspose.Total.lic")

# Set the Decod Types for the Barcode
decodeTypes=[Recognition.DecodeType.PDF_417, Recognition.DecodeType.DATA_MATRIX,
Recognition.DecodeType.QR,Recognition.DecodeType.CODE_39_EXTENDED, 
Recognition.DecodeType.CODE_128, Recognition.DecodeType.RM_4_SCC]

 # Instantiate BarCodeReader to load the Barcode image and Decode types of Barcodes to identify
BarcodeReader =  Recognition.BarCodeReader("multiple_codes.png",None, decodeTypes)

# Read the Barcodes
results = BarcodeReader.readBarCodes()

# Print the read Barcodes information
print("ReadSimpleExample:")
i = 0
while (i < len(results)):
    print(i)
    print("code text: " + results[i].getCodeText())
    print("code type: " + results[i].getCodeTypeName())
    i += 1
