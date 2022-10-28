from landing.tempToPers import tempToPers

from formatted.persistentToFormatted import persToForm

from trusted.formattedToTrusted import formattedToTrusted
from trusted.commonAreas import commonAreas
from trusted.lastOutCatImputation import lastOutCatImputation
from trusted.LSOANameImputation import lsoaNameImputation
from trusted.removeCols import removeCols
from trusted.removeDuplicates import removeDuplicates
from trusted.removeSuffixLSOAName import removeSuffix
from trusted.checkNAs import checkNAs

from exploitation.join import join

if __name__ == "__main__":
    tempToPers()
    print("Data moved from temporal to persitent\n\n")

    persToForm()
    print("Data moved from persitent to formatted\n\n")
    
    formattedToTrusted()
    print("Data moved from formatted to trusted\n\n")

    removeDuplicates()
    print("Removed duplicate cases\n\n")
    
    removeCols() 
    print("Removed unnecessary columns\n\n")

    removeSuffix() 
    print("Removed suffix from LSOA name (crimes)\n\n")

    commonAreas()
    print("Keep common districts\n\n")

    lsoaNameImputation()
    print("Impute any NAs in LSOA Name (crimes)\n\n")
    
    lastOutCatImputation() 
    print("Impute LastOutcomeCategory (crimes)\n\n")
    
    print("Checking for additional NAs\n\n")
    checkNAs()
    
    join()
    print("Joined prices and crimes tables")