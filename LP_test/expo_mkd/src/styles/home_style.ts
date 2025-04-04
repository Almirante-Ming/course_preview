import { StyleSheet } from 'react-native';

export const home_styles = StyleSheet.create({
    container: {
        flex: 1,
        backgroundColor: '#25292e',
        alignItems: 'center',
      },
    text: {
      color: '#fff',
    },
    button: {
        fontSize: 20,
        textDecorationLine: 'underline',
        color: '#fff',
      },
      imageContainer: {
        flex: 1,
        paddingTop: 28,
      },
      image: {
        width: 320,
        height: 440,
        borderRadius: 18,
      },
      footerContainer: {
        flex: 1 / 3,
        alignItems: 'center',
      },  
  });