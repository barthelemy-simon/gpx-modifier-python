# gpx-modifier-python
A small utility for runners who ever experienced a bad GPS situation. Did you ever come home after your run, only to discover that the GPS didn't work well? 

If you see your GPS didn't work well during a run, follow these instructions : This utility will only be useful if you've already made a similar run, on the same path. You'll need a .gpx file from this similar run (which will be referred as the 'reference') and the time it took you ('reference time'). You'll also need to know how much time it took you today, when your GPS didn't work well (referred as 'wanted time').

Then, with all these informations, just start Python3 directly from a terminal and type 'exec(open("Path-to-modify_gpx.py").read())' and fill the form that will be submitted to you through your terminal.

That's it, you now have a new file, which follow the same path than the reference one, but with a different time.

Also, for it to be more realist, I didn't set a linear difference time for the new file, I used the reference file, the time during 2 positions, the reference time and the wanted time to insure it won't look like you've been running at the exact same speed during the whole run. The amount of time between 2 positions in the new file is proportional to the amount of time during the reference file, following the formula : new_amount = reference_amount * (wanted_time / ref_time).
