(5.5.26 16:22)
Took a long break. Lets begin!

## Cyborg 1
cyborg1@cyborg.underthewire.tech:cyborg1
(6.5.26 14:25)

Objective: The password for cyborg2 is the state that the user Chris Rogers is from as stated within Active Directory.

This is all new to me. I'll read online a bit for what it means.

PS C:\users\cyborg1\desktop> Get-ADUser -Filter 'GivenName -eq "Chris" -and Surname -eq "Rogers"' -Properties State


DistinguishedName : CN=Rogers\, Chris\ ,OU=T-65,OU=X-Wing,DC=underthewire,DC=tech
Enabled           : False
GivenName         : Chris
Name              : Rogers, Chris
ObjectClass       : user
ObjectGUID        : ee6450f8-cf70-4b1d-b902-a837839632bd
SamAccountName    : chris.rogers
SID               : S-1-5-21-758131494-606461608-3556270690-2177
State             : kansas
Surname           : Rogers
UserPrincipalName : chris.rogers

So apperently there are properties to each user.

this gives out all  `Get-ADUser -Filter 'GivenName -eq "Chris" -and Surname -eq "Rogers"' -Properties *`

Flag: kansas

## Cyborg 2
cyborg2@cyborg.underthewire.tech:kansas

Well, this is getting into sys admin, which rn i dont mind it. Ill move to networking.
This was fun. I am not sure if its enough, but its a lot better than nothing! :)

Perhaps me using Google is cheating? IDK and IDC actually. I learned from it, and it's for my own benefit. 