import { View, StyleSheet } from 'react-native';
import { Link, Stack } from 'expo-router';
import { nfound_styles } from '../styles';

export default function NotFoundScreen() {
  return (
    <>
      <Stack.Screen options={{ title: 'Oops! Not Found' }} />
      <View style={nfound_styles.container}>
        <Link href="/" style={nfound_styles.button}>
          Go back to Home screen!
        </Link>
      </View>
    </>
  );
}


