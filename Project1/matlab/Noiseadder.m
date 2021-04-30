
for j=1:20
    filename1 = ['Wav_tennis', int2str(j), '.wav'];
    

    [y,Fs] = audioread(filename1,'native')
	%sound(y,Fs)
    t =[0:1/Fs:1-1/Fs]
    t=t.'

    for i=1:50
    noise=int16(50*rand(16000,1))
    x=y+noise;
    filename = ['Tennis',int2str(j),'_', int2str(i), '.wav'];
    
    
    
    audiowrite(filename,x,Fs)
    end
end