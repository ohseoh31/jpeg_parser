import os
import getopt
import sys
import binascii
import struct

#파일을 불러오는 함수 구현
#TODO 마커 추적 
#해당 마커부터 다음 2byte를 읽어 길이를 파악하고 해당 2byte부터 size 만큼 이동

#FFD8 ~ FFD9


#1. input 특정 폴더
#2. 폴더내의 jpg 파일 읽기
#3. 파일중 JPEG 파일 확인

#4. output JPEG 파일
'''
	2. txt akzj, offset
'''

# def load_file_list(path):


def ByteToHex( byteStr ):
    """
    Convert a byte string to it's hex string representation e.g. for output.
    """
    
    # Uses list comprehension which is a fractionally faster implementation than
    # the alternative, more readable, implementation below
    #   
    #    hex = []
    #    for aChar in byteStr:
    #        hex.append( "%02X " % ord( aChar ) )
    #
    #    return ''.join( hex ).strip()        

    return ''.join( [ "%02X " % ord( x ) for x in byteStr ] ).strip()

def help():
	print ("[-i][--input=] is input folder")
	print ("[-o][--output=] is input folder")


#ffd9 
def check_img(file):
	img_file_pointer = open(file,'rb')

	start_offset_2byte = img_file_pointer.read(2)

	sig = struct.unpack('>H', start_offset_2byte)[0]
	print (type(hex(sig))) 

	if (hex(sig) == '0xffd8'):
		print ("img")

	else :
			
		img_file_pointer.close()
		return 0

def work(input_path, output_path):
# 이미지 파일 찾기
	file_list = os.listdir(input_path)
	print (file_list)
	for file in file_list:
		print (input_path + '\\'+file)
		file_path = input_path + '\\'+file
		check_img(file_path)
		



def main():
    try:
    # 여기서 입력을 인자를 받는 파라미터는 단일문자일 경우 ':' 긴문자일경우 '='을끝에 붙여주면됨
        opts, args = getopt.getopt(sys.argv[1:],"i:f:o",["input=","help","output="])
    
    except getopt.GetoptError as err:
        print (str(err))
        help()
        sys.exit(1)

    proxy_option = 0
    input_img_path = None
    out_img_path = None
    
    if opts == [] :
        #noOption()
        help()
        sys.exit(1)

    for opt,arg in opts:

        if (opt == '-i' or opt =='--input'):
            input_img_path = arg
            '''
                unzip and insert data into database
            '''
            #load_file_list(img_path)
            # work.search(cert_path)
            # dbquery.inputIPDB()
            # sys.exit(1)
        elif ( opt == "-h") or ( opt == "--help"):
            help()
            sys.exit(1)
    work(input_img_path, out_img_path)

if __name__ == "__main__":
	# print ("test")
    main()