start = input('init?(y=1)(n=2)')
if start == 1:
    code= input('enter passcode')
    if code == 6769:
        print('confirmed')
        import serial
        import keyboard
        #import visual when found
        print('Finding peripherals')
        EEG = serial.Serial('/dev/cu.usbmodem14301',timeout=.5)
        EEG.write(01)  
        print('attempting to find headset at:',EEG.name)
        tx = 1
        while tx != 1 or 2: 
          tx = EEG.read(1)
        if tx == 1:
            print('Headset found!')
            print('testing keyboard..')
            
        else:
            print('WARNING: HEADSET MALFUNCTIONING')
            print('disconnecting headset...')
            EEG.close()
        #print('press 1 now')
            #keyboard.wait('1')
            #print('1 found! press 2 now')
            #keyboard.wait('2')
#all keyboard commands are broken.
            
          
            
        
    
else:
    print('Canselled')
