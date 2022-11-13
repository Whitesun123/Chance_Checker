from rich import print
from rich.table import Table
from rich.console import Console

console=Console()

def table_print(i,z,o,t,th,f,fi,s,se,e,n,te,el,tw,thi,fo,fif,zp,op,tp,thp,fp,fip,sp,sep,ep,np,tep,elp,twp,thip,fop,fifp):
    """ Prints a table.

    Args:
        i (int):     Number of tries
        z (int):     Number of gotten numbers
        o (int):     Number of gotten numbers
        t (int):     Number of gotten numbers
        th (int):    Number of gotten numbers
        f (int):     Number of gotten numbers
        fi (int):    Number of gotten numbers
        s (int):     Number of gotten numbers
        se (int):    Number of gotten numbers
        e (int):     Number of gotten numbers
        n (int):     Number of gotten numbers
        te (int):    Number of gotten numbers
        el (int):    Number of gotten numbers
        tw (int):    Number of gotten numbers
        thi (int):   Number of gotten numbers
        fo (int):    Number of gotten numbers
        fif (int):   Number of gotten numbers
        zp (int):    Percentage of each number
        op (int):    Percentage of each number
        tp (int):    Percentage of each number
        thp (int):   Percentage of each number
        fp (int):    Percentage of each number
        fip (int):   Percentage of each number
        sp (int):    Percentage of each number
        sep (int):   Percentage of each number
        ep (int):    Percentage of each number
        np (int):    Percentage of each number
        tep (int):   Percentage of each number
        elp (int):   Percentage of each number
        twp (int):   Percentage of each number
        thip (int):  Percentage of each number
        fop (int):   Percentage of each number
        fifp (int):  Percentage of each number
    """
    
    table = Table(title=f"Tries : {i}")                                                 # Create a table
    
    table.add_column("Numbers", justify="center", style="cyan", no_wrap=True)
    table.add_column("Results", justify="center", style="cyan", no_wrap=True)           # Create columns in table
    table.add_column("Procentige", justify="center", style="cyan", no_wrap=True)
    
    table.add_row("Zero", str(z), str(zp)+"%")
    table.add_row("One", str(o), str(op)+"%")
    table.add_row("Two", str(t), str(tp)+"%")
    table.add_row("Three", str(th), str(thp)+"%")
    table.add_row("Four", str(f), str(fp)+"%")
    table.add_row("Five", str(fi), str(fip)+"%")                                        # Create rows in table
    table.add_row("Six", str(s), str(sp)+"%")
    table.add_row("Seven", str(se), str(sep)+"%")
    table.add_row("Eight", str(e), str(ep)+"%")
    table.add_row("Nine", str(n), str(np)+"%")
    table.add_row("Ten", str(te), str(tep)+"%")
    table.add_row("Eleven", str(el), str(elp)+"%")
    table.add_row("Twelve", str(tw), str(twp)+"%")
    table.add_row("Thirteen", str(thi), str(thip)+"%")
    table.add_row("Fourteen", str(fo), str(fop)+"%")
    table.add_row("Fifteen", str(fif), str(fifp)+"%")
    
    print("\n")
    console.log(table)                                                                  # Print table