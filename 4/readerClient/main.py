import ttk
import subprocess
import Tkinter as tk

from Tkinter import *
from readerClient import readerClient

class Main:

    def __init__(self):
        #List with Cont Labels
        self.widgets = {}

        #Text widget for benchmarking
        self.benchmarkText = []

        #Host
        self.host = '192.168.56.5'

        #readerClient
        self.readerClient = readerClient(host=self.host)


    def refreshButtonPressed(self):
        logCounts = self.readerClient.getCounts()
        latestEvents = self.readerClient.getLatestEvents()
        for logType, logCount in logCounts.iteritems():
            self.widgets[logType]['text']=logCount

        for logType, logTimestamp in latestEvents.iteritems():
            self.widgets['L' + logType]['text']=logTimestamp['timestamp']

    def hostEntryButtonPressed(self):
        self.host = self.widgets['hostEntry'].get()
        self.readerClient = readerClient(host=self.host)

    def benchmark(self):
        self.widgets['bText'].delete(1.0, END)
        self.widgets['bText'].insert(END, 'Please wait, benchmarking, this can take a while...\n')
        self.widgets['bText'].update_idletasks()
        p = subprocess.Popen(['ab', '-c 10','-n 1000', self.host + '/stats'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, bufsize=1)
        for line in iter(p.stdout.readline, b''):
            self.widgets['bText'].insert(END, line)


    def prepareGUI(self):
        root = tk.Tk()
        root.title('Reader utility')

        nb = ttk.Notebook(root)

        # adding Frames as pages for the ttk.Notebook
        # first page, which would get widgets gridded into it
        page1 = ttk.Frame(nb)


        frame = ttk.LabelFrame(page1, text='Log counts and latest events')
        frame.pack()



        #Labels on first page (reader client)

        aLabel = Label(frame, text='A:')
        aLabel.grid(row=0,column=0)

        cLabel = Label(frame, text='C:')
        cLabel.grid(row=1,column=0)

        bLabel = Label(frame, text='B:')
        bLabel.grid(row=2,column=0)

        yLabel = Label(frame, text='Y:')
        yLabel.grid(row=3,column=0)

        xLabel = Label(frame, text='X:')
        xLabel.grid(row=4,column=0)

        zLabel = Label(frame, text='Z:')
        zLabel.grid(row=5,column=0)





        #Labels with log count

        aCountLabel = Label(frame, bg='green', text='A')
        aCountLabel.grid(row=0,column=1)
        self.widgets['A'] = aCountLabel

        cCountLabel = Label(frame, bg='green', text='C')
        cCountLabel.grid(row=1,column=1)
        self.widgets['C'] = cCountLabel

        bCountLabel = Label(frame, bg='green', text='B')
        bCountLabel.grid(row=2,column=1)
        self.widgets['B'] = bCountLabel

        yCountLabel = Label(frame, bg='green', text='Y')
        yCountLabel.grid(row=3,column=1)
        self.widgets['Y'] = yCountLabel

        xCountLabel = Label(frame, bg='green', text='X')
        xCountLabel.grid(row=4,column=1)
        self.widgets['X'] = xCountLabel

        zCountLabel = Label(frame, bg='green', text='Z')
        zCountLabel.grid(row=5,column=1)
        self.widgets['Z'] = zCountLabel





        #Labels with latest event

        aLatestLabel = Label(frame, bg='yellow', text='DATA')
        aLatestLabel.grid(row=0,column=2)
        self.widgets['LA'] = aLatestLabel

        cLatestLabel = Label(frame, bg='yellow', text='DATA')
        cLatestLabel.grid(row=1,column=2)
        self.widgets['LC'] = cLatestLabel

        bLatestLabel = Label(frame, bg='yellow', text='DATA')
        bLatestLabel.grid(row=2,column=2)
        self.widgets['LB'] = bLatestLabel

        yLatestLabel = Label(frame, bg='yellow', text='DATA')
        yLatestLabel.grid(row=3,column=2)
        self.widgets['LY'] = yLatestLabel

        xLatestLabel = Label(frame, bg='yellow', text='DATA')
        xLatestLabel.grid(row=4,column=2)
        self.widgets['LX'] = xLatestLabel

        zLatestLabel = Label(frame, bg='yellow', text='DATA')
        zLatestLabel.grid(row=5,column=2)
        self.widgets['LZ'] = zLatestLabel




        countRefreshButton = Button(page1, text='Refresh', command=self.refreshButtonPressed)
        #b.grid(row=6, column=0)
        countRefreshButton.pack()

        # second page
        page2 = ttk.Frame(nb)

        self.benchmarkText = Text(page2)
        self.benchmarkText.pack()

        self.widgets['bText'] = self.benchmarkText

        benchmarkButton = Button(page2, text='Run benchmark', command=self.benchmark)
        benchmarkButton.pack()


        self.benchmarkText.delete(1.0, END)

        #thirdPage
        page3 = ttk.Frame(nb)

        hostEntry = Entry(page3, width=50)
        hostEntry.pack()

        hostEntry.delete(0, END)
        hostEntry.insert(0, self.host)

        self.widgets['hostEntry'] = hostEntry

        hostEntryButton = Button(page3, text='Change host', command=self.hostEntryButtonPressed)
        hostEntryButton.pack()


        nb.add(page1, text='Client')
        nb.add(page2, text='Benchmark')
        nb.add(page3, text='Settings')

        nb.pack(expand=1, fill='both')

        root.mainloop()





if __name__ == '__main__':
    app = Main()
    app.prepareGUI()
