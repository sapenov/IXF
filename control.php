<?php

// THE CONTROL PART

require'IXFParser.php';

$in = '/tmp/export.ixf';
$out = '/tmp/out.json';

$r = (new IXFParser())->process($in,$out);

?>