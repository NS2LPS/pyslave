# Auto generated script file

V = linspace(0,1,10)
res=zeros_like(V)
fig,ax = subplots()

# Main script function
def script_main(thread):
    for i in range(len(V)):
        yoko1(V[i])
        time.sleep(1)
        res[i] = dmm1()
        ax.cla()
        ax.plot(V,res)
        data = zva.fetch()
        data.save('test.h5')
        thread.draw()
        if thread.stopflag : break
