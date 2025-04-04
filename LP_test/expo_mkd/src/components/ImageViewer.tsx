import { Image, type ImageSource } from 'expo-image';
import { home_styles } from '../styles';

type Props = {
  imgSource: ImageSource;
};

export default function ImageViewer({ imgSource }: Props) {
  return <Image source={imgSource} style={home_styles.image} />;
}
