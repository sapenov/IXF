# DB2 IXF to JSON converter

This tool was created when I needed to consume some reference data from remote DB2 z/OS into Redhat Linux environment. The DB2 Connect license was not properly configured, so consuming data directly in Java or PHP client was not an option. Another problem was that DB2 z/OS doesn't provide ways to export result set into CSV format, providing the only option - get file as PC/IXF format.

After some reading, I came up with some code that converts IXF file into perfectly valid JSON.

To get started, you can just drop IXF file and two coverter files in same folder (I picked /tmp but feel free pick any other folder) and run following command:

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

```
## License

The MIT License (MIT)

Copyright (c) 2017 Khazretgali Sapenov

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
