# DB2 IXF to JSON converter

This tool was created when I needed to import some reference data from remote DB2 z/OS into Redhat Linux environment. The DB2 Connect license was not properly configured on the host, so consuming data directly in Java or PHP clients was not an option. Another problem was that DB2 z/OS doesn't provide ways to export result set into CSV format, providing the only option - get file as PC/IXF format.

After some reading, I came up with a code, that converts IXF file into perfectly valid JSON.

To get started, you can just drop IXF file and two converter files in same folder (I picked /tmp but feel free pick any other folder) and run following command:

```
php control.php
```
If it runs without errors, you should find out.json in the same directory.

If you want to change file names, feel free to edit 'in' and 'out' variables in control.php

```php

<?php

// THE CONTROL PART

require'IXFParser.php';

$in = '/tmp/export.ixf';
$out = '/tmp/out.json';

$r = (new IXFParser())->process($in,$out);

?>
