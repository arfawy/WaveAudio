import struct

class Wave:    
    def __init__(self, filename):
        self.filename = filename
        f = open(filename,"rb")
        #Bloc de déclaration d'un fichier au format WAVE
        self.fileTypeBlocID = self.ascii(f.read(4))
        self.fileSize = struct.unpack('<L', f.read(4))[0]
        self.fileFormatID = self.ascii(f.read(4))

        #Bloc décrivant le format audio
        self.formatBlocID = self.ascii(f.read(4))
        self.blocSize = struct.unpack('<L', f.read(4))[0]
        self.audioFormat = struct.unpack('<h', f.read(2))[0]
        self.nbrCanaux = struct.unpack('<h', f.read(2))[0]
        self.frequence = struct.unpack('<L', f.read(4))[0]
        self.bytePerSec = struct.unpack('<L', f.read(4))[0]
        self.bytePerBloc = struct.unpack('<h', f.read(2))[0]
        self.bitsPerSample = struct.unpack('<h', f.read(2))[0]

        #Bloc des données
        self.dataBlocID = self.ascii(f.read(4))
        self.dataSize = struct.unpack('<L', f.read(4))[0]
        self.datas = list(f.read(self.dataSize))
        f.close()

    def ascii(cls, bi):
        l = list(bi)
        ll = []
        for i in range(len(l)):
            ll.append(chr(l[i]))
        return "".join(ll)
    
    def getParams(self):
        return {
            "FileTypeBlocID":self.fileTypeBlocID,
            "FileSize":self.fileSize,
            "FileFormatID":self.fileFormatID,
            "FormatBlocID":self.formatBlocID,
            "BlocSize":self.blocSize,
            "AudioFormat":self.audioFormat,
            "NbrCanaux":self.nbrCanaux,
            "Frequence":self.frequence,
            "BytePerSec":self.bytePerSec,
            "BytePerBloc":self.bytePerBloc,
            "BitsPerSample":self.bitsPerSample,
            "DataBlocID":self.dataBlocID,
            "DataSize":self.dataSize
            }
      
wave = Wave("angry_dog.wav")
print (wave.getParams())
