import json
"""
Description: This class converts DB2 PC / IXF file into JSON file.
@ param1
int
@ param2
string
@ param3
boolean
@ return object
with
"""

class IXFParser:

    def __init__(self, i, o):
        self.mem = "500M"
        self.i = i
        self.o = o
    
    def get_header(self, feed, start):
        # read offsets into dict
        # print(" Start reading header section for feed ")

        offsets = {
        'IXFHRECL': 6,
        'IXFHRECT' : 1,
        'IXFHID' : 3,
        'IXFHVERS': 4,
        'IXFHPROD' : 12,
        'IXFHDATE':8,
        'IXFHTIME': 6,
        'IXFHHCNT': 5,
        'IXFHSBCP' : 5,
        'IXFHDBCP' : 5,
        'IXFHFIL1' : 2
        }

        ret = self.conv(feed, start, offsets)
        return ret    
    
    
    def get_table(self, feed, start):
    
            offsets = {
                'IXFTRECL' : 6,
                'IXFTRECT' : 1,
                'IXFTNAML' : 3,
                'IXFTNAME' : 256,
                'IXFTQULL' : 3,
                'IXFTQUAL' : 256,
                'IXFTSRC' : 12,
                'IXFTDATA' : 1,
                'IXFTFORM' : 1,
                'IXFTMFRM' : 5,
                'IXFTLOC' : 1,
                'IXFTCCNT' : 5,
                'IXFTFIL1' : 2,
                'IXFTDESC' : 30,
                'IXFTPKNM' : 257,
                'IXFTDSPC' : 257,
                'IXFTISPC' : 257,
                'IXFTLSPC' : 257
                }

            # print(" Start reading table section for feed ")
            ret = self.conv(feed, start, offsets)

            return ret

    
    def get_column_descriptor(self, feed, start):
        offsets = {
        'IXFCRECL' : 6,
        'IXFCRECT' : 1,
        'IXFCNAML' : 3,
        'IXFCNAME' : 256,
        'IXFCNULL' : 1,
        'IXFCDEF' : 1,
        'IXFCSLCT' : 1,
        'IXFCKPOS' : 2,
        'IXFCCLAS' : 1,
        'IXFCTYPE' : 3,
        'IXFCDBCP' : 5,
        'IXFCLENG' : 5,
        'IXFCDRID' : 3,
        'IXFCPOSN' : 6,
        'IXFCDESC' : 30,
        'IXFCLOBL' : 20,
        'IXFCUDTL' : 3,
        'IXFCUDTN' : 256,
        'IXFCDEFL' : 3,
        'IXFCDEFV' : 254,
        'IXFCREF' : 1,
        'IXFCNDIM' : 2,
        'IXFCDSIZ' : 1
        }
   
        #print(" Start reading column section for feed ")
        ret = self.conv(feed, start, offsets)

        return ret
   

    def get_data(self, feed, start):
        offsets = {
            'IXFDRECL' : 6,
             'IXFDRECT' : 1,
             'IXFDRID' : 3,
             'IXFDFIL1' : 4,
             'IXFDCOLS' : 1
            }
        ret = self.conv(feed, start, offsets)
    
        return ret
    
   
    def get_meta(self, feed):
    
        hstart = 0
        h = self.get_header(feed, hstart)
        tstart = 6 + h['IXFHRECL']
        t = self.get_table(feed, tstart)
    
        numColumns = int(t["IXFTCCNT"])
        # print(f"We have {numColumns} columns.")
    
        cstart = 6 + tstart + t['IXFTRECL']
        s = cstart
        
        for i in range(0, numColumns):        
            c[i] = self.get_column_descriptor(feed, s)
            s += c[i]['IXFCRECL'] + 6

            ret['recLength'] = 0
            for v in c:
                columnName = v['IXFCNAME'].strip()
                recLength = int(v['IXFCRECL'])
                columnLength = int(v['IXFCLENG'])
                ret[columnName] = columnLength
                ret['recLength'] += columnLength            
                ret['start'] = s
        
        return ret               
            
            
    def conv(self, feed, start, offsets):
    
        fp = fopen(feed, 'r')        
        fseek(fp, start, SEEK_SET)
        
        for k, v in offsets.items():
        
            # last column of COLUMNDESCRIPTOR
            if k == 'IXFCDSIZ':   
                lv = int(ret['IXFCRECL']) - 868
                ret[k] = fread(fp, lv)
                ret['pointer'] = ftell(fp)
                
            # last column of DATA COL                
            elif k == 'IXFDCOLS': 
                #print("\ret['IXFDRECL'] = ".ret['IXFDRECL'])
                # lv2 = int(ret['IXFDRECL']) - 14
                lv2 = int(ret['IXFDRECL'] - 8)
                ret[k] = fread(fp, lv2)
                ret['pointer'] = ftell(fp)
                
            else:                
                ret[k] = fread(fp, v) # read chunk
                
        return ret
        
    
    
    def process(f, outfile):
    
        m = self.getMeta(f)
        # ini_set('memory_limit',self.mem)
        st = m["start"]
        out = {}
        n = 0
                      
        while d["IXFDRECT"] != "D":
            n = n + 1
            d = self.getData(f, st)

            out[n]["PRODUCT_KEY"] = substr(d["IXFDCOLS"], 0, 11).strip()
            out[n]["REVENUE_DIVISION"] = substr(d["IXFDCOLS"], 12, 2).strip()
            out[n]["KEY_PRODUCT_ID"] = substr(d["IXFDCOLS"], 14, 4).strip()
            out[n]["DESCRIPTION"] = substr(d["IXFDCOLS"], 18, 40)

            st = d['pointer']
            json = json_dumps(out, sort_keys=True, indent=4)
            with open(outfile, "a") as myfile:
                myfile.write(json)
    
        return n
