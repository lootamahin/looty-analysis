import re

class ParseStats:

    def __init__(self, stats):
        self.stats = stats

    def return_stats_html(self):
        #Remove [, ], <newlines> and quotations
        self.stats = re.sub(r'\[|\]|\n|\"', '', self.stats)
        #Remove all occurrences of one or more spaces
        self.stats = re.sub(' +', '', self.stats)
        #Replace },{ with [START] to serve as an easier to view/use split marker
        self.stats = re.sub('\},\{', '\n[START]\n', self.stats)
        #Remove the first occurrence only of {
        self.stats = self.stats.replace("{", "", 1)        
        
#SAMPLE TEXT:
#playerStatSummaryType:AramUnranked5x5,wins:45,modifyDate:1397308828000,aggregatedStats:{totalTurretsKilled:26,totalAssists:1797,totalChampionKills:738}
        
        # We want to replace the "," and ":" within the { } for "aggregatedStats".
        # Otherwise, we can't parse the data correctly within the for loop below
        JAGTEST = self.stats
        JAGTEST = re.sub('\{.*\}', lambda x:x.group(0).replace(',',';'), JAGTEST)
        JAGTEST = re.sub('\{|\}', '|', JAGTEST)
        
#MODIFIED SAMPLE TEXT:
#aggregatedStats:|totalTurretsKilled:26;totalChampionKills:738;totalAssists:1797|,modifyDate:1397308828000,playerStatSummaryType:AramUnranked5x5,wins:45
        
        donger_this_shit = JAGTEST.split("[START]")
        
        purtyhtml = ""
        gametype_header = ""
        allotherstats_block = ""
        aggstats_block = ""
        statsdata_all = ""
        i = 0
                
        for donger in donger_this_shit:
            dongturd = donger.split(',') # dongturd[] = all parts in donger separated by a ","
            
            for dongturdchunk in dongturd: # EX: = aggregatedStats:|totalTurretsKilled:26;totalChampionKills:738;totalAssists:1797|
                if "aggregatedStats" in dongturdchunk:
                    dongturdchunk = dongturdchunk.replace("|", "")
                    dongturdchunk = dongturdchunk.replace("aggregatedStats:", "")
                    
                    if ":" in dongturdchunk:
                        eachstatset = dongturdchunk.split(';')
                        aggstats_block = aggstats_block + "<br><b><u>AGGREGATED STATS:</u></b><br>\n"
                        
                        for eachstat in eachstatset:
                            tinystats = eachstat.partition(':')
                            aggstats_block = aggstats_block + "<b>AS: " + tinystats[0] + ":</b> <i>" + tinystats[2] + "</i><br>\n"

                    else:
                        aggstats_block = "<br>NO AGG STATS HERE!!!"
                        
                else:
                    dongturdchunkdrop = dongturdchunk.partition(':') #EX: modifyDate:1397308828000
                    
                    if "playerStatSummaryType" in dongturdchunkdrop[0]:
                        gametype_header = gametype_header + "<br><b><u>GAME TYPE:</u></b> " + dongturdchunkdrop[2] + "<br>\n"
                        
                    else:
                        allotherstats_block = allotherstats_block + "<b>" + dongturdchunkdrop[0] + ":</b> " + dongturdchunkdrop[2] + "<br>\n"

            #statsdata_all += gametype_header + allotherstats_block + "<font size=\"10\">" + aggstats_block + "</font><br>&nbsp;<br><b>" + str(i) + "</b><br>&nbsp;<br>"
            statsdata_all += gametype_header + "\n" + allotherstats_block + "\n<font size=\"2\">" + aggstats_block + "</font>\n<br>&nbsp;<br>\n\n"
            gametype_header = ""
            allotherstats_block = ""
            aggstats_block = ""
            i += 1
             
        #self.stats = "<html>\n<body>\n<font face=\"Arial\">\n" + self.stats + "\n</font>\n</body>\n</html>\n\n\n\n<br>&nbsp;<br>\n\n\n\n" + JAGTEST + "\n\n\n\n<br>&nbsp;<br>\n\n\n\n<font face\"Arial\">" + purtyhtml
        #self.stats = "<html>\n<body>\n<font face=\"Arial\">\n" + self.stats + "\n\n\n\n<br>&nbsp;<br>\n\n\n\n<font face\"Arial\">" + JAGTEST + "\n\n\n\n<br>&nbsp;<br>\n\n\n\n<font face\"Arial\">" + statsdata_all
        self.stats = "<html>\n<body>\n<font face=\"Arial\">\n" + statsdata_all + "</font>\n</body>\n</html>"
        self.stats = self.stats.replace("|", "")
        response = self.stats
        
        return response
        
        
        
        
        
        
        
        