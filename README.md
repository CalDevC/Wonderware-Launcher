# Wonderware-Launcher
A python program that will launch Wonderware software (window maker and window viewer) on monitors with different resolutions than the resolution that the project was originally created on without converting the project

# The Problem
Wonderware projects are created using a certain resolution monitor. When attempting to open Wonderware software such as window maker and window viewer while using a monitor that has a different resolution than the original, Wonderware will make you convert the project to open it. When you convert the project, however, the interfaces you have designed can be shifted around causing your project to no longer display properly on monitors that different resolutions. This issue arises when the display you are developing or editing on is a different resolution than the displays you are deploying on.

The real problem lies within Wonderware itself, but since there's nothing we can do about that we have to find a way around the problem. The 2 solutions I have found thus far are either:

1. Have a second monitor that is the same resolution as the displays you are deploying to and make that display your main display before launching window maker or window viewer and then change your main display back.

2. Change the resolution of your monitor to match the resolution of the screens you are deploying to and then change it back.

# The Solution
Since we can't fix the source of the issue, we'll just automate the work around. This program adds a couple macros to your command prompt that are used to launch either window maker or window viewer. When used, they will automatically change the resolution of your screen to the resolution of your deployment screen, launch your selected application, and then return the resolution back to what it was originally.

The macros:
  maker  - launches window maker
  viewer - launches window viewer

# Usage Instructions
After cloning the repo some initial set up is required, however, I've tried to make it as simple as possible. The set up steps are:

  1. Open the vars.py file and fill out the required variables. Each one has a comment explaining what it is
  2. Use the command prompt to navigate into the repo's directory and run the command 'python set_up.py'

That completes the initial set up. your macros should now be active and can be used from any where in the command prompt.

The macros:
  maker  - launches window maker
  viewer - launches window viewer

# Troubleshooting
If you see your screen going black (this is because it is updating the resolution) but Wonderware is till asking for you to convert your resolution then one of two things is happening:

  1. You are not converting to the proper resolution.
       
      Fix: Check the variable 'WW_RES' in the vars.py file. It should have two numbers that match the resolution numbers that Wonderware is asking for.

      Ex: If Wonderware is expecting 1280x1024 then WW_RES = ['1280', '1024']

  2. The Wonderware software is taking longer than expected to launch. (The resolution is being converted back before Wonderware starts booting)
      
      Fix: You can extend the duration of time between launching Wonderware and reverting the resolution by changing the variable 'WAIT_TIME' in the vars.py file. This number is how many seconds to wait before converting the resolution back.
