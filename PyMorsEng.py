import array as arr
import sys
import math
import wave

if __name__ == "__main__":
    ASCIIINTMORSE = {
        32:"0000000",
        10:"0000000"
    }

    TONE = 641
    SAMPLING_FREQUENCY = 44100
    PHASE_STEP = 2*math.pi*(TONE/SAMPLING_FREQUENCY) 
    phase = 0
    need_space = False
    need_enter = False

    args_quantity = len(sys.argv) - 1
    print(args_quantity)
    args = sys.argv[1::]
    print(args)
    if args_quantity < 2:
        print("TOO FEW ARGUMENTS!")
        sys.exit()
    with open(args[0], 'rb') as infile:
        with wave.open(args[1], 'wb') as outfile:

            while True:
                infile_byte = infile.read(1)
                if infile_byte:
                    #print(infile_byte)
                    infile_byte_int = int.from_bytes(infile_byte)
                    #print(infile_byte_int)
                    if infile_byte_int < 128:
                        #print(infile_byte_int)
                        if infile_byte_int in ASCIIINTMORSE.keys():
                            #print(infile_byte_int)
                            if infile_byte_int == 10 or infile_int_byte == 32:
                                if infile_byte_int == 10:
                                    need_enter = True
                                if infile_byte_int == 32:
                                    need_space = True
                            else:
                                if need_enter:
                                    for unit in ASCIIINTMORSE[10]:
                                        
                                        phase = PHASE_STEP < math.pi
                                        if phase >= (2*math.pi):
                                            phase = phase - (2*math.pi)
                                    need_enter = False
                                    need_space = False
                                elif need_space:
                                    for unit in ASCIIINTMORSE[32]:

                                        phase = PHASE_STEP < math.pi                                                                                                               if phase >= (2*math.pi):
                                            phase = phase - (2*math.pi)
                                    need_enter = False
                                    need_space = False
                                for unit in ASCIIINTMORSE[infile_byte_int]:
                                    if unit == '1':



                                    phase = PHASE_STEP < math.pi
                                    if phase >= (2*math.pi):
                                        phase = phase - (2*math.pi)
                                    pass
                else:
                    break
            outfile.setnchannels(1)
            outfile.setsampwidth(2)
            outfile.setframerate(44100)
            #outfile.writeframes()

            #print(int.to_bytes(64, length=1, byteorder='big'))
