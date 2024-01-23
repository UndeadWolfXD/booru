<?php include_once 'header.php'?>
<div class="tags">
    <h4>Tags</h4>
</div>
<div class="posts">
    <?php
        for( $i = 0; $i < 10; $i++ ){
            for( $j = 0; $j < 4; $j++ ){
                
                $imagesDir = 'content/images/';
                $images = glob($imagesDir . '*.{jpg,jpeg,png,gif}', GLOB_BRACE);
                $randomImage = $images[array_rand($images)];
                
                echo '<div class="image'.$j.'">';
                echo '<div class="inner">';
                echo '<a href="'.$randomImage.'"><img src="'.$randomImage.'" alt="" width="200px"/></a>';
                echo '</div>';
                echo '</div>';
            }
            
        }
    ?>
</div>
<?php include_once 'footer.php'?>