import os
import random
from rich import print
from rich.table import Table
from rich.console import Console
console = Console()
from cogs.table_print import table_print            # From main directory > cogs.table_print
from cogs.graph_make import graphMaker

class Guess:
    def guesser(R):
        """Tries to throw 15 heads (1) in a row.

        Args:
            R (bool): If R == True, then show a graph otherwise pass
        """
        
        i   = 0             # Loops
        
        z   = 0             # Zero
        o   = 0             # One
        t   = 0             # Two
        th  = 0             # Three
        f   = 0             # Four
        fi  = 0             # Five
        s   = 0             # Six
        se  = 0             # Seven
        e   = 0             # Eight
        n   = 0             # Nine
        te  = 0             # Ten
        el  = 0             # Eleven
        tw  = 0             # Twelve
        thi = 0             # Thirteen
        fo  = 0             # Fourteen
        fif = 0             # Fifteen
        
        while True:
            i += 1
            
            r1 = random.randint(0, 1)
            r2 = random.randint(0, 1)
            r3 = random.randint(0, 1)
            r4 = random.randint(0, 1)
            r5 = random.randint(0, 1)                   # Gets random number 1 == heads | 0 == tails
            r6 = random.randint(0, 1)
            r7 = random.randint(0, 1)
            r8 = random.randint(0, 1)
            r9 = random.randint(0, 1)
            r10 = random.randint(0, 1)
            r11 = random.randint(0, 1)
            r12 = random.randint(0, 1)
            r13 = random.randint(0, 1)
            r14 = random.randint(0, 1)
            r15 = random.randint(0, 1)
            result = r1 + r2 + r3 + r4 + r5 + r6 + r7 + r8 + r9 + r10 + r11 + r12 + r13 + r14 + r15        # Combines all the numbers together
            
            print(f"Current loop > {i} < {r1}:{r2}:{r3}:{r4}:{r5}:{r6}:{r7}:{r8}:{r9}:{r10}:{r11}:{r12}:{r13}:{r14}:{r15} = {result}")
            
            if result == 0:
                z += 1
            elif result == 1:
                o += 1
            elif result == 2:
                t += 1
            elif result == 3:
                th += 1
            elif result == 4:
                f += 1
            elif result == 5:
                fi += 1
            elif result == 6:
                s += 1
            elif result == 7:
                se += 1
            elif result == 8:
                e += 1
            elif result == 9:
                n += 1
            elif result == 10:
                te += 1
            elif result == 11:
                el += 1
            elif result == 12:
                tw += 1
            elif result == 13:
                thi += 1
            elif result == 14:
                fo += 1
            elif result == 15:
                fif += 1
                break
        
        zp = round(z / i * 100, 2)                      
        op = round(o / i * 100, 2)
        tp = round(t / i * 100, 2)
        thp = round(th / i * 100, 2)
        fp = round(f / i * 100, 2)
        fip = round(fi / i * 100, 2)                    # Calculates the percentage of each number
        sp = round(s / i * 100, 2)
        sep = round(se / i * 100, 2)
        ep = round(e / i * 100, 2)
        np = round(n / i * 100, 2)
        tep = round(te / i * 100, 2)
        elp = round(el / i * 100, 2)
        twp = round(tw / i * 100, 2)
        thip = round(thi / i * 100, 2)
        fop = round(fo / i * 100, 2)
        fifp = round(fif / i * 100, 2)
        
        table_print(i,z,o,t,th,f,fi,s,se,e,n,te,el,tw,thi,fo,fif,zp,op,tp,thp,fp,fip,sp,sep,ep,np,tep,elp,twp,thip,fop,fifp)   # Send variables to function
        
        if R == True:
            graphMaker(i,zp,op,tp,thp,fp,fip,sp,sep,ep,np,tep,elp,twp,thip,fop,fifp)