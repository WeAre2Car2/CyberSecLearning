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

|Goal|Command|
|---|---|
|**Count Files Only**|`(Get-ChildItem -File).Count`|
|**Count All Items** (Files + Folders)|`(Get-ChildItem).Count`|
|**Recursive Count** (Subfolders included)|`(Get-ChildItem -File -Recurse).Count`|
|**Count Specific Types** (e.g., .txt)|`(Get-ChildItem -Filter *.txt).Count`|
|**Include Hidden/System Files**|`(Get-ChildItem -File -Force).Count`|

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