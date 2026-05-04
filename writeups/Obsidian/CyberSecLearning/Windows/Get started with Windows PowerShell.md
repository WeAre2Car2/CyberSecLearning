4.5.26 14:45

# Learn about Windows PowerShell

PowerShell is an automation solution that consists of a command-line shell, a scripting language, and a configuration-management framework.

## Command-line shell

Windows PowerShell superseded the Windows command-line interface (**cmd.exe**) and the limited functionality of its batch file scripting language. PowerShell accepts and returns .NET objects and includes:

- A command-line history.
- Tab completion and prediction.
- Support for command and parameter aliases.
- Chaining commands that use the Pipeline feature.
- A robust in-console help system

## A scripting language

_Commands_ provide PowerShell’s main functionality. There are many varieties of commands, including cmdlets (pronounced _command-lets_), functions, filters, scripts, applications, configurations, and workflows. Commands are building blocks that you piece together by using the Windows PowerShell scripting language. Using commands enables you to create custom solutions to complex administrative problems. Alternatively, you can run commands directly within the PowerShell console to complete a single task. The console is the CLI for PowerShell and is the primary way in which you'll interact with PowerShell.

==Cmdlets use a Verb-Noun naming convention. For example, you can use the **Get-Command** cmdlet to list all cmdlets and functions that are registered in the command shell==. The verb identifies the action for the cmdlet to perform, and the noun identifies the resource on which the cmdlet will perform its action.

Microsoft server applications and cloud services provide specialized cmdlets that you can use to manage those services. In fact, you can manage some features _only_ by using PowerShell. In many cases, even when the application provides a graphical user interface (GUI) to manage a specific functionality, it relies on PowerShell to implement at least some of its features behind the scenes.

So far, I understand that PowerShell, next gen CMD.exe is a cross platform CLI automation tool that has a scripting language and a shell of its own. You can write scripts that make windows do stuff. Many apps built by Microsoft that are GUI based actually use PowerShell under the hood.

I just found out about UnderTheWire! PowerShell CTFs!!
After finishing this training, Ill play around this website :)

The training is quite technical. I dont plan to be a sysadmin, so maybe it's not exactly for me. At least not ALL of it. I look like a poser who switches tech stack every day. I promise I am not. I think?
