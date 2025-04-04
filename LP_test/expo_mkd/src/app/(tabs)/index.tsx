import { View } from 'react-native';
import { home_styles } from '../../styles';

import { Button, ImageViewer } from '../../components';

const PlaceholderImage = require('@assets/images/background-image.png');

export default function Index() {

  return (
    <View style={home_styles.container}>
      <View style={home_styles.imageContainer}>
        <ImageViewer imgSource={PlaceholderImage} />
      </View>
        <View style={home_styles.footerContainer}>
        <Button label="Choose a photo" />
        <Button label="Use this photo" />
      </View>
    </View>
  );
}