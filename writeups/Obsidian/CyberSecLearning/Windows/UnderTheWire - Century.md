## Century 1
century1@century.underthewire.tech:century1

Objective: recieve the password from the powershell build. After a quick Google search I found this command: **`$PSVersionTable`**
Lets run it.
Name                           Value
----                           -----
PSVersion                      5.1.14393.8957
PSEdition                      Desktop
PSCompatibleVersions           {1.0, 2.0, 3.0, 4.0...}
BuildVersion                   ==10.0.14393.8957==
CLRVersion                     4.0.30319.42000
WSManStackVersion              3.0
PSRemotingProtocolVersion      2.3
SerializationVersion           1.1.0.1

Lets test it.

flag: 10.0.14393.8957

## Century 2
century2@century.underthewire.tech:10.0.14393.8957

Objective: The password for Century3 is the name of the built-in cmdlet that performs the wget like function within PowerShell PLUS the name of the file on the desktop.

So I ran dir, which is like ls in windows. I got this:

PS C:\users\century2\desktop> dir


    Directory: C:\users\century2\desktop


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        8/30/2018   3:29 AM            693 ==443==

So we have the second part, which is 443.

I searched "wget like in powershell" and got:
"In PowerShell, the equivalent of Linux's `wget` is the **`Invoke-WebRequest`** cmdlet"

so the password should be ==invoke-webrequest443==. It is stated that the password will always be lowercased.

flag: invoke-webrequest443

## Century 3

century3@century.underthewire.tech:invoke-webrequest443

I am taking a break after this. My back hurts.

Objective: The password for Century4 is the number of files on the desktop.

I searched "powershell num of files in current dir" and got:

```
(Get-ChildItem -File).Count
```

also: 

Quick Reference Commands

| Goal                                      | Command                                |
| ----------------------------------------- | -------------------------------------- |
| **Count Files Only**                      | `(Get-ChildItem -File).Count`          |
| **Count All Items** (Files + Folders)     | `(Get-ChildItem).Count`                |
| **Recursive Count** (Subfolders included) | `(Get-ChildItem -File -Recurse).Count` |
| **Count Specific Types** (e.g., .txt)     | `(Get-ChildItem -Filter *.txt).Count`  |
| **Include Hidden/System Files**           | `(Get-ChildItem -File -Force).Count`   |

Important Tips

- **Performance for Large Folders**: If you have millions of files, use the faster .NET method:  
    `[System.IO.Directory]::GetFiles($PWD).Count`.
- **PowerShell Versions**:
    - **PS 3.0+**: The `.Count` property works even if the folder contains 0 or 1 item.
    - **Older versions**: You must wrap the command in `@()` (e.g., `@(Get-ChildItem).Count`) to ensure it returns an array.
- **Handling Errors**: If a folder is empty, `.Count` might return nothing instead of `0`. To fix this, pipe to `Measure-Object`:  
    `Get-ChildItem -File | Measure-Object | Select-Object -ExpandProperty Count`.

lets run it. we get a count of 123.

flag: 123

## Century 4

century4@century.underthewire.tech:123

Objective: The password for Century5 is the name of the file within a directory on the desktop that has spaces in its name.

There is the desktop named "Can you open me". inside there is a file named "15768" which containes: "Great Work!  Keep it up."

the directory has spaces in its name, so I assume that the password is "15768".
It is the password. I guess we learned to cd.

flag: 15768

## Century 5

century5@century.underthewire.tech:15768

Objective: The password for Century6 is the short name of the domain in which this system resides in PLUS the name of the file on the desktop.

Lets find the other half first.

full log:
Windows PowerShell
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!
PS C:\users\century5\desktop> dir


    Directory: C:\users\century5\desktop


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        8/30/2018   3:29 AM             54 ==3347==


PS C:\users\century5\desktop> Get-Content .\3347
Don't forget to get the Short Domain name in lowercase
PS C:\users\century5\desktop> (Get-CimInstance Win32_ComputerSystem).Domain
==underthewire==.tech

I guess that this will be the domain based on the ssh login, but just to make sure. 

flag: underthewire3347

## Century 6
(4.5.26 19:05)
century6@century.underthewire.tech:underthewire3347

Objective: The password for Century7 is the number of folders on the desktop.

I assume the command needed to enter is quite similar to Century 3

I assume `(Get-ChildItem -Folder).Count` is correct, similar to the solution of said level. lets test that.
It did not work. Apparently its -Directory.
Payload: `(Get-ChildItem -Directory).Count`
We get 197.

flag: 197

## Century 7
century7@century.underthewire.tech:197

Objective: The password for Century8 is in a readme file somewhere within the contacts, desktop, documents, downloads, favorites, music, or videos folder in the user’s profile.

My first instinct is to try to grep it. like find a file named readme systemwide.

payload: Get-ChildItem -Path "C:\users\century7" -Filter "readme.txt" -Recurse -File -ErrorAction SilentlyContinue

-Recurse will also look is subfolders. ErrorAction SilentlyContinue will not print Access Denied.

`PS C:\users\century7\desktop> Get-ChildItem -Path "C:\users\century7" -Filter "readme.txt" -Recurse -File -ErrorAction SilentlyContinue`


    `Directory: C:\users\century7\Downloads`


`Mode                LastWriteTime         Length Name`
`----                -------------         ------ ----`
`-a----        8/30/2018   3:29 AM              7 Readme.txt`


`PS C:\users\century7\desktop> Get-Content C:\users\century7\Downloads\readme.txt`
`7points`

flag: 7points

## Century 8
century8@century.underthewire.tech:7points

Objective: The password for Century9 is the number of unique entries within the file on the desktop.

My first instinct is to grep by unique lines. I know that is possible.
A search on google gave me this: `Select-String -Pattern "Error" -Path .\unique.txt | Group-Object Line -NoElement | Select-Object Count, Name`

it didnt return anything. maybe the answer is zero?

I looked up again. Found this: `(Get-Content "C:\path\to\file.txt" | Select-Object -Unique).Count`
This makes a lot more sense.
Payload: `(Get-Content "C:\users\century8\desktop\unique.txt" | Select-Object -Unique).Count`
We get 696.

Flag: 696
## Century 9
century9@century.underthewire.tech:696

Objective: The password for Century10 is the 161st word within the file on the desktop.

There has to be a command to search by line number. 
I read through this: [Select-String (Microsoft.PowerShell.Utility) - PowerShell | Microsoft Learn](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/select-string?view=powershell-7.6)

Then here: [How to print a certain line of a file with PowerShell? - Stack Overflow](https://stackoverflow.com/questions/14759649/how-to-print-a-certain-line-of-a-file-with-powershell/14759794#14759794)

Lets try some commands.

`PS C:\users\century9\desktop> (Get-Content Word_File.txt)[161]
`i`

Lets test if this is the answer. It was not.

Lets try `get-content Word_File.txt | select -first 1 -skip 160

Also did not work.

I am so dumb. Its by words, not lines... My god.

`(Get-Content -Raw "C:\users\century9\desktop\Word_File.txt" -ErrorAction SilentlyContinue).Split(" `r`n", [System.StringSplitOptions]::RemoveEmptyEntries)[160]
`
I kinda understand what it does. Lets try it. 

payload: `PS C:\users\century9\desktop> (Get-Content -Raw "C:\users\century9\desktop\Word_File.txt" -ErrorAction SilentlyContinue).Split(" rn", [System.StringSplitOptions]::RemoveEmptyEnt`
`ries)[160]`
`pierid`

flag: pierid
`
## Century 10
(5.4.26 13:47)
century10@century.underthewire.tech:pierid

Objective: The password for Century11 is the 10th and 8th word of the Windows Update service description combined PLUS the name of the file on the desktop.

Seams easy enough. Lets see how can we find this message.
This seems to be a service. I found a command called `Get-Service`.
We can specify the name by adding -Name. A google search helped me find this: `Get-Service -Name wuauserv`

Lets run it.

`Get-CimInstance -ClassName Win32_Service -Filter "Name='wuauserv'" | Select-Object Name, Description` really seems to do the job. The other one just listed the service.
I also ran dir and got a file named "110".

Flag: windowsupdates110

## Century 11
century11@century.underthewire.tech:windowsupdates110

Objective: The password for Century12 is the name of the hidden file within the contacts, desktop, documents, downloads, favorites, music, or videos folder in the user’s profile.

I thought immediately to search recursively and show hidden files. ill cd into the user folder. Ill include the whole level here:

Get-ChildItem -Recurse -Hidden 

I remember there is a way to shut the errors off. -ErrorAction SilentlyContinue

Get-ChildItem -Recurse -Hidden -ErrorAction SilentlyContinue

Flag: secret_sauce

## Century 12
century12@century.underthewire.tech:secret_sauce

Objective: The password for Century13 is the description of the computer designated as a Domain Controller within this domain PLUS the name of the file on the desktop.

Lets start with the easy one. Running dir:
\_things

The other part. The computer designated as a Domain Controller within that domain... Lets search what is that. Thank god for Google and AI!

`Get-ADComputer -Filter 'ObjectClass -eq "computer" -and userAccountControl -band 8192' -Properties Description | Select-Object Name, Description

This command does that. Do I know what it does by heart? No way.

Flag: i_authenticate_things

## Century 13
century13@century.underthewire.tech:i_authenticate_things

Objective: The password for Century14 is the number of words within the file on the desktop.

There has to be an easy command for listing the words on a file. We solved a challenge yesterday with that, so lets try to not even search.

(Get-Content countmywords.txt).Count doesnt work.

Get-Content "countmywords" | Measure-Object -Word
Piping it through Measure-Object by words might work. Found it on google.
We got "755".

## Century 14
century14@century.underthewire.tech:755

Objective: The password for Century15 is the number of times the word “polo” appears within the file on the desktop.
Searching on Google gave me this command: `(Get-Content "C:\path\to\file.txt" | Select-String -Pattern "\bYourWord\b" -AllMatches).Matches.Count

so: `(Get-Content countpolos | Select-String -Pattern "\bpolo\b" -AllMatches).Matches.Count
"153"

Flag: 153

## Century 15
century15@century.underthewire.tech:153

Objective: Well there is no objective. I finished Century! It was fun but easy. Unless restricting to only reading docs, a quick google search gave me the results and I knew how to tinker it. Maybe because cli isn't completely new to me. Well, I will continue with this website. its 14:44 now. I will push it and take a break.