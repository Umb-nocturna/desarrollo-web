<?php
$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://umb-web2-production.up.railway.app/estudiante',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'GET',
  CURLOPT_POSTFIELDS => array('codigo' => '1001294969'),
));


$response = curl_exec($curl);
curl_close($curl);
$data = json_decode($response, true);

if ($data && isset($data['frase'])) {
    $value_data = $data['frase'][0];
} else {
    $value_data =  "No se pudo obtener la frase.";
}

?>

<!DOCTYPE html>
<html>
<body>

<h1>My First API integration</h1>
<p>My phrase.
<?php echo $value_data; ?>
</p>

</body>
</html>