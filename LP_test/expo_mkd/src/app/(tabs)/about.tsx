import { Text, View, StyleSheet } from 'react-native';
import { about_styles } from '../../styles';

export default function AboutScreen() {
  return (
    <View style={about_styles.container}>
      <Text style={about_styles.text}>About screen</Text>
    </View>
  );
}

