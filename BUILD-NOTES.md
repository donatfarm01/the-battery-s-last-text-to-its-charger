Build notes for the battery's last text entry.

The idea came from reading the judge brief first. The judge wants a real joke whose turn lands in the final words, a voice that sounds like a person typing to a charger, and an angle beyond the obvious dying battery complaint. So the line is not about the battery running out. It is about the battery keeping score all day while the charger walks past it and charges the AirPods case first, then spending its last percent on a spiteful parting shot at the case.

The entry is one fixed line held in the program itself, because the sandbox has no network and the text is the whole entry. The program only creates the output folder, writes that line to the entry file with no trailing newline, and sets the file readable by everyone so the grader can collect it.

I checked the line by counting its characters and by running the program locally, then reading the output file back and hashing it two ways. The local kit check was run on the repository afterwards.
