#!/usr/bin/env python
# encoding:UTF-8
# rainbowsUnicorns.py
r"""
    Summary
    =======
    This python module does some amazing things.

    The primary job of the module is to spawn unicorns and rainbows.

    The *main* function is the primary controlling function
    for this module. All other functions are called from it.

    Use
    ===
    The script is used two different ways.

    1. Create unicorns.
    2. Create rainbows.

    .. IMPORTANT:: You must spawn a rainbow before creating unicorns or they will fall
          to the ground without anything to stand on or fly over.

    Developer(s)
    ============
    Rainbow Developer

    Support Person(s)
    =================
    ============  ====================  ===========  ==========  ==========================
      Priority         ame                Primary      Backup              Role
    ------------  --------------------  -----------  ----------  --------------------------
         1         Unicorn wrangler          X                     Application Programmer
         2         Rainbow cleaner                        X        Database Editor
    ============  ====================  ===========  ==========  ==========================

    Users
    ===================
    ======================  ====================  ============================
      Department              Contact Person               Use
    ----------------------  --------------------  ----------------------------
      Marketing              Sarah Sellsalot       Show the world the magic.
      Finance                Payme Now             Collect the cash.
      Development            Ova Workd             Spawn magic on demand.
    ======================  ====================  ============================

    Application Type
    ================
    Script

    Language
    ========
    Python

    Source Control Location
    =======================
    - \\\\localShare\\Development\\rainbowsUnicorns.py - Primary script - development version.
    - \\\\serverShare\\Deployment\\rainbowsUnicorns.py - Primary script - deployment version.
    - \\\\serverShare\\Deployment\\starDust.py - Globally used functions for all deployed modules.
    - \\\\erverShare\\Deployment\\Log_Files:   Location of log files.

    Deployment Technology
    =====================
    Script can be run using Pyscripter or Sublimetext. No installer required.

    Deployment Location / Location of Installation Files
    ====================================================
    Same as Source Control Location. No media required.

    Application Prerequisites
    =========================
    - Python version 2.7 required.
    - Folder location of python.exe and python\\scripts folder needs to be
      added to the Path of the system's Environment variables.
    - Script has dependencies on modules from starDust.py in the Source Control
       Location.
    - The following Python modules must be installed on the system: pyodbc.

    Installation Instructions / Issues
    ==================================
    Not Applicable


    External Resources / Dependencies
    =================================
    None

    Security
    ========
    Database access granted through database connection strings.

    Reporting
    =========
    Script log file is created in \\\\erverShare\\Deployment\\Log_Files folder each time the script is run. Format is
    rainbowsUnicorns_YYYYMMDD_HHMMSS.txt.

    Development Prerequisites
    =========================
    None

    Glossary
    ========
    .. _pyodbc connection: https://code.google.com/p/pyodbc/wiki/Connection
    .. _pyodbc cursor: https://code.google.com/p/pyodbc/wiki/Cursor

    Script Procedure Overview
    =========================
    - Python and starDust custom python modules imported.
    - 'main()' function called to execute the script and call the other
      functions.
    - Get the name of this file for use in log file.
    - Set local variables.
    - Create a log file.
    - Count the number of unicorns and rainbows and add more to the world.
    - Create more unicorns and rainbows as necessary.

    Publisher
    =========
    Office of Unicorns and Rainbows

    Created
    =======
    20150409

    Last Revised
    ============
    20150410

    Change Log / Release Notes
    ==========================
    +----------+-------------------------------------------------------------+
    | YYYYMMDD |  DESCRIPTION                                                |
    +==========+=============================================================+
    | 20150410 | Increased quantity of rainbows spawned.                     |
    +----------+-------------------------------------------------------------+
    | 20150410 | Increased quantity of unicorns spawned.                     |
    +----------+-------------------------------------------------------------+

    Functions
    =========
"""

# IMPORT NECESSARY PYTHON MODULES AND CUSTOM FUNCTIONS IN THE starDust MODULE
try:
    import datetime # Date and time modules.
    import gc       # Garbage collector.
    import inspect  # Need for inspection.
    import os       # Operating System Modules.
    import random   # Used to generate random numbers.
    import sys      # System module.



    # SET THE PYTHONDONTWRITEBYTECODE ENVIRONMENT VARIABLE
    # TO TRUE SO THAT IT WILL NOT CREATE COMPILED PYTHON (PYC) FILES
    # WHEN IMPORTING OTHER PY FILES.
    sys.dont_write_bytecode = True

    # IMPORT starDust THAT CONTAINS CUSTOM FUNCTIONS
    # import starDust

except:
    print "Import of modules failed. Exiting script."
    # EXIT SCRIPT
    sys.exit()


# ----------------------------------------------------------
# FUNCTION DEFINITION SECTION
#
# DEFINE MAJOR FUNCTIONS THAT ARE USED THROUGHOUT THE PROGRAM.
#
# ----------------------------------------------------------
def addUnicorn(currentCount, numNeeded):
    """ Print the number of unicorns in the world and then add more using the 
        quantity passed into the function.

        Bacon ipsum dolor amet short loin strip steak landjaeger pastrami, alcatra fatback rump shoulder pork loin t-bone tail sirloin. Swine sausage beef pastrami porchetta shank kevin alcatra short ribs beef ribs. Boudin biltong rump kielbasa chuck turkey beef. Shoulder shankle chicken, leberkas filet mignon beef ribs frankfurter t-bone pork turkey ball tip pork chop jerky. Tenderloin pastrami tongue ground round spare ribs, venison ham swine pork chop fatback kevin pork tri-tip pig. T-bone tongue bresaola, pork chop landjaeger kielbasa jerky chicken ground round prosciutto alcatra shoulder ham.

        .. WARNING:: You must spawn a rainbow before creating unicorns or they will fall
          to the ground without anything to stand on or fly over.

        :param numNeeded: The quantity of new unicorns to create.
        :type numNeeded: int
        :param happyMessage: Message to the user.
        :type happyMessage: str     
    """
    try:
        happyMessage = "You're so special because you created rainbows and unicorns."

        # Print the number of unicorns there are now and how many we'll create.
        print("We have %s unicorns shedding happiness on the world." % (currentCount))
        print("We're going to add %s more!!" % numNeeded)
        
        # Loop through the quantity of unicorns needed
        # and create new ones.
        for newUnicorn in range(numNeeded):
          print("Creating a new unicorn.")
          print("We must create a rainbow first.")
          addRainbow()
          
          # Increase unicorn count.
          currentCount += 1
          print("We just created another 4 legged bundle of joy.\r\r")

        # Print totals and message.
        print("Now we have %s unicorns." % (currentCount))
        print(happyMessage)
       
    except:
        print("So sad, we had a problem creating the unicorn.")



def addRainbow():
    """ Add more rainbows to the world.

        :param numRainbows: Random quantity between 1 and 15 of new rainbows to create.
        :type numRainbows: int
        :param happyMessage: Message to the user.
        :type DBConn: str 

    """
    try:
        # Set the number of rainbows to create.
        numRainbows = random.randint(1,15)
        print("There are never enough rainbows! :)")
        try:
            print("We just made %s more!!" % (numRainbows))
            print("Done making the world a better place.")
        except:
            print("We had a problem making the rainbow. We're out of magic.")
    except:
        print("Something is terribly wrong in the world. We failed creating a rainbow.  :(") 
        # GARBAGE COLLECT VARIABLES
        gc.collect()
        # EXIT SCRIPT
        sys.exit()
    pass


def setVariables():
    """ Sets the variables used throughout the program.

        .. NOTE:: Many variables are imported from :py:func:`starDust`.

        :param scriptDescription: Task that this script completes.
        :type scriptDescription: str
        :param textLog: Name of the log file to document this script.
        :type textLog: str
        :param thisFilesName: Name of the module that is currently running.
        :type thisFilesName: str

    """
    try:
        print("Create variables.\r\r")        

        global scriptDescription
        scriptDescription = "We are working to make the world a better place."

        # USE THE CURRENT SCRIPT'S NAME, WITH THE .PY SLICED FROM THE END,
        # THEN ADD THE DATE AND USE AS THE LOG FILES NAME.
        global textLog
        textLog = thisFilesName[:-3] + "_" + (datetime.datetime.now()).strftime("%Y%m%d_%H%M%S") + ".txt"
    except:
        print("Error initializing variables - Exiting script.")
        # GARBAGE COLLECT VARIABLES
        gc.collect()
        # EXIT SCRIPT
        sys.exit()
    pass



def main():
    """ Primary function that calls all the other functions to execute
        the program.

        :param thisFilesName: Name of the module that is currently running.
            Obtained by inspection of the current frame.
        :type thisFilesName: str

        :param currentUnicornCount: Quantity of unicorns that currently exist.
        :type currentUnicornCount: int
        :param newUnicornsNeeded: Random quantity between 1 and 55 of new unicorns to create.
        :type newUnicornsNeeded: int
    """
    # Get the filename of this script.
    global thisFilesName
    thisFilesName = os.path.basename(inspect.getfile(inspect.currentframe()))

    print "Setting local variables... -- setVariables function."
    setVariables()

    # Set unicorn parameters.
    currentUnicornCount = 2
    newUnicornsNeeded = random.randint(1,5)

    # Create some unicorns.
    addUnicorn(currentUnicornCount, newUnicornsNeeded)

    print "\r"
    #  GARBAGE COLLECT VARIABLES
    gc.collect()
    print "SCRIPT FINISHED."


if __name__ == '__main__':
    # CALL THE MAIN FUNCTION
    main()