# How to Detect Canary and Seed Microsoft Office Files with Python Without Triggering an Alert

 ## Introduction: 

In the realm of cybersecurity, vigilance is key. One way malicious actors might infiltrate systems is through seemingly innocuous Microsoft Office files. These files might contain hidden URLs or macros designed to execute harmful actions. In this blog post, we'll explore a Python script designed to detect potentially suspicious Microsoft Office documents by examining their contents without opening them directly, reducing the risk of inadvertently triggering malicious code.

## Understanding the Script:

### The script operates in several steps: 

- Identification: It first identifies whether a given file is a Microsoft Office document (specifically, with .docx, .xlsx, or .pptx extensions). These types of files are essentially zip archives containing various XML and other files, which can be programmatically examined.

- Decompression and Scanning: Once identified, the script renames the file to a .zip extension and decompresses it into a temporary directory. It then scans through the decompressed contents, looking for URLs using regular expressions. URLs can sometimes indicate external resources or links to malicious sites.

- Ignoring Certain URLs: Not all URLs are malicious. Many Office documents contain standard schema or namespace URLs that are part of the file's structure. The script includes an ignored_domains list to filter out these benign URLs, focusing only on the unexpected or potentially harmful ones.

- Flagging Suspicious Files: If the script finds URLs not on the ignored list, it marks the file as suspicious. This is a heuristic approach and should be tailored according to the specific security context and threat model of your environment.

- Cleanup and Restoration: After scanning, the script cleans up by deleting the temporary decompressed files and renames the original file back to its initial extension, ensuring no residual clutter or changes.

![detecting canary tokens and seed files](https://github.com/Lupovis/DetectingCanaryTokens/assets/998733/08625785-7958-444f-aeac-ac5887e10981)

## Using the Script: 

- To use the script, you need a basic Python environment and some understanding of file paths and regular expressions. Here's how you can deploy and utilize this script:

- Setup: Ensure Python is installed on your system. Place the script in a convenient location and update the `PATH_TO_CHECK` variable to point to the file or directory you want to examine.

- Run: Execute the script. It will print out any URLs found in the documents it examines, flagging any document containing unexpected URLs as suspicious.

- Interpret: Review the output. Remember, this script is a starting point — not all flagged documents are necessarily malicious, and not all malicious documents will be flagged. Always follow up with manual review and additional security measures.
